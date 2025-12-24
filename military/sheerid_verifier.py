"""ChatGPT 军人 SheerID 认证器"""
import json
import random
import re
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

import httpx

from .config import (
    DEFAULT_MILITARY_STATUS,
    MILITARY_ORGANIZATIONS,
    METADATA_FLAGS,
    SUBMISSION_OPT_IN
)
from .name_generator import generate_name, generate_email


class SheerIDVerifier:
    """SheerID 军人认证处理器"""

    def __init__(self, verification_id: str, program_id: str):
        self.verification_id = verification_id
        self.program_id = program_id
        self.base_url = "https://services.sheerid.com/rest/v2"

    @staticmethod
    def parse_verification_id(url: str) -> Optional[str]:
        """从 URL 中解析 verificationId"""
        patterns = [
            r'verificationId=([a-f0-9\-]+)',
            r'/verify/[^/]+/\?verificationId=([a-f0-9\-]+)',
            r'verification/([a-f0-9\-]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None

    @staticmethod
    def parse_program_id(url: str) -> Optional[str]:
        """从 URL 中解析 programId"""
        pattern = r'/verify/([a-f0-9]+)'
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        return None

    def _generate_birth_date(self) -> str:
        """生成出生日期（18-65岁之间）"""
        today = datetime.now()
        min_age = 18
        max_age = 65
        age = random.randint(min_age, max_age)
        
        birth_year = today.year - age
        birth_month = random.randint(1, 12)
        birth_day = random.randint(1, 28)
        
        return f"{birth_year}-{birth_month:02d}-{birth_day:02d}"

    def _generate_discharge_date(self) -> str:
        """生成退役日期（1-30年前）"""
        today = datetime.now()
        years_ago = random.randint(1, 30)
        days_offset = random.randint(0, 365)
        
        discharge_date = today - timedelta(days=years_ago * 365 + days_offset)
        return discharge_date.strftime("%Y-%m-%d")

    def _step1_collect_military_status(self) -> Dict[str, Any]:
        """第一步：收集军人状态"""
        url = f"{self.base_url}/verification/{self.verification_id}/step/collectMilitaryStatus"
        
        payload = {
            "status": DEFAULT_MILITARY_STATUS
        }
        
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://services.sheerid.com",
            "Referer": f"https://services.sheerid.com/verify/{self.program_id}/"
        }
        
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.post(url, json=payload, headers=headers)
                response.raise_for_status()
                result = response.json()
                
                return {
                    "success": True,
                    "submission_url": result.get("submissionUrl"),
                    "current_step": result.get("currentStep"),
                    "data": result
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def _step2_submit_personal_info(self, submission_url: str) -> Dict[str, Any]:
        """第二步：提交个人信息"""
        # 生成随机信息
        first_name, last_name = generate_name()
        email = generate_email(first_name, last_name)
        birth_date = self._generate_birth_date()
        discharge_date = self._generate_discharge_date()
        organization = random.choice(MILITARY_ORGANIZATIONS)
        
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "birthDate": birth_date,
            "email": email,
            "phoneNumber": "",
            "organization": {
                "id": organization["id"],
                "name": organization["name"]
            },
            "dischargeDate": discharge_date,
            "locale": "en-US",
            "country": "US",
            "metadata": {
                "marketConsentValue": False,
                "refererUrl": "",
                "verificationId": self.verification_id,
                "flags": json.dumps(METADATA_FLAGS),
                "submissionOptIn": SUBMISSION_OPT_IN
            }
        }
        
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://services.sheerid.com",
            "Referer": f"https://services.sheerid.com/verify/{self.program_id}/"
        }
        
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.post(submission_url, json=payload, headers=headers)
                response.raise_for_status()
                result = response.json()
                
                return {
                    "success": True,
                    "verification_id": result.get("verificationId"),
                    "current_step": result.get("currentStep"),
                    "email": email,
                    "name": f"{first_name} {last_name}",
                    "organization": organization["name"],
                    "birth_date": birth_date,
                    "discharge_date": discharge_date,
                    "data": result
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def verify(self) -> Dict[str, Any]:
        """执行完整的军人认证流程"""
        try:
            # 第一步：收集军人状态
            step1_result = self._step1_collect_military_status()
            if not step1_result["success"]:
                return {
                    "success": False,
                    "error": f"第一步失败: {step1_result.get('error')}",
                    "step": "collectMilitaryStatus"
                }
            
            submission_url = step1_result.get("submission_url")
            if not submission_url:
                return {
                    "success": False,
                    "error": "未获取到提交URL",
                    "step": "collectMilitaryStatus"
                }
            
            # 第二步：提交个人信息
            step2_result = self._step2_submit_personal_info(submission_url)
            if not step2_result["success"]:
                return {
                    "success": False,
                    "error": f"第二步失败: {step2_result.get('error')}",
                    "step": "collectInactiveMilitaryPersonalInfo"
                }
            
            # 检查是否需要文档上传
            current_step = step2_result.get("current_step", "")
            pending = "docUpload" in current_step or "review" in current_step.lower()
            
            return {
                "success": True,
                "pending": pending,
                "verification_id": step2_result.get("verification_id"),
                "email": step2_result.get("email"),
                "name": step2_result.get("name"),
                "organization": step2_result.get("organization"),
                "birth_date": step2_result.get("birth_date"),
                "discharge_date": step2_result.get("discharge_date"),
                "current_step": current_step,
                "message": "认证提交成功，等待审核" if pending else "认证已完成"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "step": "unknown"
            }
