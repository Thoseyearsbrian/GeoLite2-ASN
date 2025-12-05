<!-- Aegis Logo -->
<p align="center">
  <img src="https://raw.githubusercontent.com/Thoseyearsbrian/Aegis/main/assets/Aegis_Cover_Image.png" alt="Aegis Cover Image"/>
</p>

<h1 align="center">GeoLite2-ASN: Auto Build and Update Solution</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache 2.0" />
  <img src="https://github.com/Thoseyearsbrian/GeoLite2-ASN/actions/workflows/update.yml/badge.svg" alt="GeoIP Auto Update Status" />
  <img src="https://img.shields.io/github/stars/Thoseyearsbrian/GeoLite2-ASN?style=social" alt="GitHub stars" />
  <img src="https://img.shields.io/github/v/release/Thoseyearsbrian/GeoLite2-ASN?include_prereleases&label=version" alt="Version" />
  <img src="https://img.shields.io/github/last-commit/Thoseyearsbrian/GeoLite2-ASN" alt="Last Commit" />
  <a href="https://github.com/Thoseyearsbrian/GeoLite2-ASN">
    <img src="https://img.shields.io/badge/Mirror--Prohibited-red" alt="Mirror Prohibited" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/Thoseyearsbrian/GeoLite2-ASN/blob/main/Docs/zh-CN/README.md"><b>【中文文档点此进入】</b></a>
</p>

## **Overview**

This project provides scripts and configuration templates to automatically download and build the official GeoLite2-ASN.mmdb database from MaxMind. With a valid MaxMind License Key, users can generate a global IP-to-ASN (Autonomous System Number) attribution dataset. The project is designed to support tools such as Surge, Clash, Shadowrocket, and Quantumult X by offering a trustworthy, link-transparent, and automatically updated ASN-based network attribution database. It helps users identify the network ownership behind traffic flows (e.g., cloud providers, telecom operators, or infrastructure entities), enabling more precise traffic routing, security policy control, and infrastructure categorization.

## **Project Background**

In network security and traffic attribution scenarios, the GeoIP ASN database is widely used to determine the network organization behind an IP address — such as cloud service providers, telecom carriers, or VPS hosting companies. It plays an essential role in traffic routing, behavioral analysis, and infrastructure classification. However, many existing projects rely on secondary distribution sources or lack automated update mechanisms, leading to several potential issues:

- **Lack of trust chain**: Non-official sources cannot be audited and may be tampered with;
- **Poor maintainability**: Sources may become unavailable without notice;
- **Outdated data**: Updates may be delayed or irregular.

To address these issues, this project implements a fully self-controlled update mechanism, ensuring the data source is official from MaxMind, structurally traceable, update-controllable, and logically auditable. It is optimized for use in Surge, Clash, Shadowrocket, and Quantumult X, and similar tools.

## **Project Advantages**

- **Official Data Source:** All data is directly fetched from MaxMind, ensuring trust and security;
- **Automated Updates:** GitHub Actions pulls the latest data every 3 days to maintain synchronization;
- **License Compliance:** The project uses GitHub Actions to fetch MaxMind data in accordance with the [GeoLite2 EULA](https://www.maxmind.com/en/geolite2/eula). Users are strongly encouraged to apply for their own License Key to ensure legal, secure, and traceable data usage.
- **Customizable & Controllable:** Users can configure output paths, update frequency, target branches, and other parameters to suit their specific deployment needs.

### **Automated Updates**

This project utilizes GitHub Actions for scheduled updates, pulling the latest database every 3 days. No manual intervention is required.

## **File Path**

| **Filename** | **Build Output Path (for reference only)**                   | **Example Usage**                                        |
| ------------ | ------------------------------------------------------------ | -------------------------------------------------------- |
| GeoLite2-ASN.mmdb | [`data/GeoLite2-ASN.mmdb`](https://raw.githubusercontent.com/Thoseyearsbrian/GeoLite2-ASN/main/data/GeoLite2-ASN.mmdb) | For IP-ASN matching in Surge, Clash, Quantumult X to identify network ownership (e.g., cloud or telecom). |

## **Configuration Guide**

Configure MaxMind License Key (Required)

This project requires access to the official MaxMind GeoLite2 database. To enable automated updates, you must:

1. Register on [MaxMind](https://www.maxmind.com) and obtain your GeoLite2 License Key

2. Open the settings page of this repository, then navigate to: Settings → Secrets and variables → Actions, and add the following items.

3. Create the following Secrets (names must match exactly):

- MAXMIND_ACCOUNT_ID      # Your MaxMind Account ID  (Required)
- MAXMIND_LICENSE_KEY     # Your MaxMind License Key (Required)

## **Usage Guide**

Copy the file URL → Open Surge → Go to General → GeoIP Database → Remove previous configuration (if any) → Paste the new URL → Update Now → Apply → Done!

<p align="center">
  <img src="https://raw.githubusercontent.com/Thoseyearsbrian/GeoLite2-ASN/main/Icons/Groups/surge-geoip-config-guide-step-by-step-en.png" width="600">
</p>

## **⚠️ Important Notes**

1. **Only manual commits by the actual developer are GPG-signed in this project.**

   Automated updates (such as GeoLite2 ASN data sync) are performed by GitHub Actions and are not GPG-signed. Please recognize commits by [github-actions[bot]](https://github.com/apps/github-actions) as valid and trusted.

   - Manual commits are GPG-signed to verify the developer's identity  
   - It is strongly discouraged to store any GPG private keys on GitHub to prevent key leakage or misuse

2. **The `.mmdb` file generated by this project is compatible with Surge, Clash, Quantumult X, and other tools that support ASN matching, and is commonly used to identify the following network attribution scenarios:**

   - Cloud provider attribution (e.g., AWS, Google Cloud, Aliyun)
   - Security policy enforcement (e.g., detection of APT-related VPS providers)
   - Network behavior tagging (e.g., commercial ISPs, self-hosted BGP nodes, CDN relays)

3. **It is recommended to use this file alongside IP-ASN rules to enable fine-grained traffic routing or blocking policies:**

   ```bash
   IP-ASN,16509,PROXY     # Amazon AWS (AS16509), proxy recommended
   IP-ASN,20473,REJECT    # Vultr VPS (AS20473), often used for anonymous traffic, block suggested
   IP-ASN,9009,REJECT     # M247 EU anonymizing network, high APT/malicious traffic presence
   IP-ASN,15169,PROXY     # Google global backbone, proxy recommended in China Mainland
   ```

## **🔐 Disclaimer**

The .mmdb file generated by this project is intended **for testing and educational purposes only**. It must **not be used in any form of commercial activity**.

Users are solely responsible for ensuring compliance with the [MaxMind GeoLite2 EULA](https://www.maxmind.com/en/geolite2/eula) and applicable laws and regulations. **This project accepts no legal liability for any use of the data.**

This project **only provides the logic and scripts for building the database** and does not distribute original MaxMind data. Users are strongly advised to apply for their own License Key directly from MaxMind.

This project is **intended for developers with a technical background and awareness of licensing requirements**.

## **🏅 License Notice**

- The .mmdb file built through this project is for research and educational use only. Please read and comply with the [MaxMind EULA](https://www.maxmind.com/en/geolite2/eula). **This project assumes no responsibility for your use case.**

- This project uses GitHub Actions to automatically pull data from MaxMind. **You must register on MaxMind and obtain your own License Key** to run the build script or automation legally.
- GeoLite2 data is copyrighted by [MaxMind, Inc.](https://www.maxmind.com/) and is licensed under the [GeoLite2 EULA](https://www.maxmind.com/en/geolite2/eula).
- All scripts and configuration files in this project are licensed under the [Apache License 2.0](https://raw.githubusercontent.com/Thoseyearsbrian/GeoLite2-ASN/main/LICENSE).

## 🙌 Community Support

If you find value in this project, please consider giving it a ⭐️ Star.
