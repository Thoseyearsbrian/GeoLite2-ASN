#!/usr/bin/env python3
"""
# 下载并解压 MaxMind 官方 GeoLite2-ASN.mmdb 数据库

- 自动读取 MAXMIND_LICENSE_KEY 环境变量
- 支持本地使用 .env 文件（用于本地开发）
- 从 MaxMind 官方地址下载 GeoLite2-ASN 压缩包
- 解压出 .mmdb 文件至 ./release 目录
"""

import os
import requests
import tarfile
from pathlib import Path

# 支持本地开发使用 .env 文件
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parent.parent / '.env'
    load_dotenv(env_path)
except ImportError:
    pass

license_key = os.getenv("MAXMIND_LICENSE_KEY")

if not license_key:
    raise SystemExit("未找到 MAXMIND_LICENSE_KEY，请设置环境变量或提供 .env 文件")

# 下载 URL
url = (
    "https://download.maxmind.com/app/geoip_download"
    f"?edition_id=GeoLite2-ASN&license_key={license_key}&suffix=tar.gz"
)

tar_path = "GeoLite2-ASN.tar.gz"
output_dir = "release"

print("开始从 MaxMind 下载 GeoLite2-ASN 数据库...")
print(f"下载地址: {url}")

try:
    r = requests.get(url, stream=True)
    r.raise_for_status()

    with open(tar_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

    print("下载完成")
except Exception as e:
    raise SystemExit(f"下载失败: {e}")

os.makedirs(output_dir, exist_ok=True)

# 解压 mmdb 文件
try:
    with tarfile.open(tar_path, "r:gz") as tar:
        for member in tar.getmembers():
            if member.name.endswith(".mmdb"):
                member.name = os.path.basename(member.name)
                tar.extract(member, output_dir, numeric_owner=False)

    print(f".mmdb 文件已解压至 {output_dir}/")
except Exception as e:
    raise SystemExit(f"解压失败: {e}")
finally:
    os.remove(tar_path)
    print("临时文件已删除")