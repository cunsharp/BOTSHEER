"""军人认证配置"""

# SheerID 配置
PROGRAM_ID = "YOUR_PROGRAM_ID_HERE"  # 需要从 ChatGPT 军人认证页面获取

# 军人状态选项
MILITARY_STATUS_OPTIONS = [
    "VETERAN",      # 退伍军人
    "ACTIVE_DUTY",  # 现役
    "RESERVE"       # 预备役
]

# 默认使用 VETERAN（退伍军人）
DEFAULT_MILITARY_STATUS = "VETERAN"

# 军队组织列表
MILITARY_ORGANIZATIONS = [
    {"id": 4070, "name": "Army"},              # 陆军
    {"id": 4073, "name": "Air Force"},         # 空军
    {"id": 4072, "name": "Navy"},              # 海军
    {"id": 4071, "name": "Marine Corps"},      # 海军陆战队
    {"id": 4074, "name": "Coast Guard"},       # 海岸警卫队
    {"id": 4544268, "name": "Space Force"}     # 太空军
]

# 元数据配置
METADATA_FLAGS = {
    "doc-upload-considerations": "default",
    "doc-upload-may24": "default",
    "doc-upload-redesign-use-legacy-message-keys": False,
    "docUpload-assertion-checklist": "default",
    "include-cvec-field-france-student": "not-labeled-optional",
    "org-search-overlay": "default",
    "org-selected-display": "default"
}

SUBMISSION_OPT_IN = (
    'By submitting the personal information above, I acknowledge that my personal information '
    'is being collected under the <a target="_blank" rel="noopener noreferrer" '
    'class="sid-privacy-policy sid-link" href="https://openai.com/policies/privacy-policy/">'
    'privacy policy</a> of the business from which I am seeking a discount, and I understand '
    'that my personal information will be shared with SheerID as a processor/third-party service '
    'provider in order for SheerID to confirm my eligibility for a special offer. '
    'Contact OpenAI Support for further assistance at support@openai.com'
)
