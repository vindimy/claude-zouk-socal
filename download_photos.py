#!/usr/bin/env python3
"""Download Instagram profile photos using the mobile API."""

import os
import time
import json
import urllib.request
import urllib.error

IMAGES_DIR = "/Users/dv/Library/CloudStorage/Dropbox/Dev/claude-zouk-socal/images"

PROFILES = [
    ("aneskafranca",    "images/aneska-franca.jpg"),
    ("adamjcraig",      "images/adam-j-craig.jpg"),
    ("stonganie",       "images/stephanie-tong.jpg"),
    ("mylaosa",         "images/myla-ostroshenko.jpg"),
    ("christinazouk",   "images/christina-montoya.jpg"),
    ("braydenzouk",     "images/brayden-schmidt.jpg"),
    ("sarahzouk",       "images/sarah-miles.jpg"),
    ("marissa.a.rivera","images/marissa-a-rivera.jpg"),
    ("nathy.carbajal",  "images/nathalia-carbajal.jpg"),
    ("nyamaste",        "images/dmitriy-vi.jpg"),
    ("broc.co.ly",      "images/ly-le.jpg"),
    ("cococonnects",    "images/corina-post.jpg"),
    ("amastrus_music",  "images/matt-laney.jpg"),
    ("djcal_z",         "images/orlan-mat.jpg"),
    ("dhroovvy",        "images/dhruv-puri.jpg"),
]

BASE_DIR = "/Users/dv/Library/CloudStorage/Dropbox/Dev/claude-zouk-socal"
MIN_SIZE = 1024  # 1 KB

MOBILE_HEADERS = {
    "User-Agent": "Instagram 219.0.0.12.117 Android (26/8.0.0; 480dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 314665256)",
    "Accept": "*/*",
    "Accept-Language": "en-US",
    "X-IG-App-ID": "936619743392459",
    "X-IG-Capabilities": "3brTvw==",
    "Connection": "keep-alive",
}

def fetch_profile_pic_url(username):
    """Fetch profile pic URL via Instagram mobile API."""
    api_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    req = urllib.request.Request(api_url, headers=MOBILE_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw = resp.read()
            data = json.loads(raw)
            user = data.get("data", {}).get("user", {})
            url = user.get("profile_pic_url_hd") or user.get("profile_pic_url")
            return url
    except urllib.error.HTTPError as e:
        print(f"  API HTTP error {e.code}: {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"  API URL error: {e.reason}")
        return None
    except Exception as e:
        print(f"  API error: {e}")
        return None

def download_image(url, dest_path):
    """Download image from url to dest_path."""
    img_headers = dict(MOBILE_HEADERS)
    img_headers["User-Agent"] = (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
    )
    req = urllib.request.Request(url, headers=img_headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        with open(dest_path, "wb") as f:
            f.write(data)
        return len(data)
    except Exception as e:
        print(f"  Download error: {e}")
        return 0

successes = []
failures = []

for username, rel_path in PROFILES:
    dest_path = os.path.join(BASE_DIR, rel_path)
    print(f"\n--- {username} -> {rel_path} ---")

    # Skip if already downloaded
    if os.path.exists(dest_path):
        size = os.path.getsize(dest_path)
        if size > MIN_SIZE:
            print(f"  Already exists ({size:,} bytes), skipping.")
            successes.append((username, rel_path, size))
            continue
        else:
            print(f"  Exists but too small ({size} bytes), re-downloading.")

    # Step 1: get profile pic URL
    print(f"  Fetching profile pic URL for @{username}...")
    pic_url = fetch_profile_pic_url(username)

    if not pic_url:
        print(f"  FAILED: could not retrieve profile pic URL.")
        failures.append((username, rel_path, "No URL from API"))
        time.sleep(2)
        continue

    print(f"  Got URL: {pic_url[:80]}...")

    # Step 2: download image
    print(f"  Downloading image...")
    size = download_image(pic_url, dest_path)

    if size > MIN_SIZE:
        print(f"  SUCCESS: {size:,} bytes saved.")
        successes.append((username, rel_path, size))
    else:
        msg = f"File too small or empty ({size} bytes)"
        print(f"  FAILED: {msg}")
        failures.append((username, rel_path, msg))
        if os.path.exists(dest_path):
            os.remove(dest_path)

    # Be polite to Instagram's servers
    time.sleep(2)

# Summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"\nSuccessful downloads ({len(successes)}/{len(PROFILES)}):")
for username, rel_path, size in successes:
    print(f"  [OK] @{username:20s} -> {rel_path}  ({size:,} bytes)")

if failures:
    print(f"\nFailed downloads ({len(failures)}/{len(PROFILES)}):")
    for username, rel_path, reason in failures:
        print(f"  [FAIL] @{username:20s} -> {rel_path}  ({reason})")
else:
    print("\nNo failures!")

print(f"\nTotal: {len(successes)} succeeded, {len(failures)} failed.")
