#!/usr/bin/env python3
"""
API Documentation Test Script

This script tests all three endpoints from the Product Recommendation API:
1. POST /generate_api_key - Generate authentication key
2. POST /query - Get product recommendations 
3. POST /send - Store arbitrary JSON data

Usage: python3 test_api_docs.py
"""

import requests
import json
import sys
from datetime import datetime


# API Configuration
BASE_URL = "https://jgypz1bf15gb8c-8000.proxy.runpod.net"
HEADERS = {"Content-Type": "application/json"}


def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")


def print_result(endpoint, status, response_data, error=None):
    """Print formatted test results"""
    status_symbol = "✅" if status == "SUCCESS" else "❌"
    print(f"{status_symbol} {endpoint}: {status}")
    
    if error:
        print(f"   Error: {error}")
    else:
        print(f"   Response: {json.dumps(response_data, indent=2)}")


def test_generate_api_key():
    """Test the /generate_api_key endpoint"""
    print_section("Testing POST /generate_api_key")
    
    try:
        payload = {"username": f"test-key-{datetime.now().strftime('%Y%m%d-%H%M%S')}"}
        
        response = requests.post(
            f"{BASE_URL}/generate_api_key",
            headers=HEADERS,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            api_key = data.get("api_key")
            
            if api_key:
                print_result("/generate_api_key", "SUCCESS", data)
                return api_key
            else:
                print_result("/generate_api_key", "FAILED", data, "No API key in response")
                return None
        else:
            print_result("/generate_api_key", "FAILED", {}, f"HTTP {response.status_code}: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print_result("/generate_api_key", "ERROR", {}, str(e))
        return None


def test_query_endpoint(api_key):
    """Test the /query endpoint"""
    print_section("Testing POST /query")
    
    if not api_key:
        print_result("/query", "SKIPPED", {}, "No API key available")
        return False
    
    try:
        headers = {**HEADERS, "X-API-Key": api_key}
        payload = {
            "basket_query": "blue trucker hat\nblack snapback\nsummer sale"
        }
        
        response = requests.post(
            f"{BASE_URL}/query",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            
            # Validate response structure
            if "ids" in data and "basket_query" in data:
                print_result("/query", "SUCCESS", data)
                return True
            else:
                print_result("/query", "FAILED", data, "Missing expected fields in response")
                return False
        else:
            print_result("/query", "FAILED", {}, f"HTTP {response.status_code}: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print_result("/query", "ERROR", {}, str(e))
        return False


def test_send_endpoint(api_key):
    """Test the /send endpoint"""
    print_section("Testing POST /send")
    
    if not api_key:
        print_result("/send", "SKIPPED", {}, "No API key available")
        return False
    
    try:
        headers = {**HEADERS, "X-API-Key": api_key}
        payload = {
            "event": "api_documentation_test",
            "timestamp": datetime.now().isoformat(),
            "test_id": f"test-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            "rating": 5,
            "comment": "Automated test of API documentation"
        }
        
        response = requests.post(
            f"{BASE_URL}/send",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get("status") == "stored":
                print_result("/send", "SUCCESS", data)
                return True
            else:
                print_result("/send", "FAILED", data, "Unexpected response status")
                return False
        else:
            print_result("/send", "FAILED", {}, f"HTTP {response.status_code}: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print_result("/send", "ERROR", {}, str(e))
        return False


def main():
    """Run all API tests"""
    print("🚀 Starting API Documentation Tests")
    print(f"📍 Base URL: {BASE_URL}")
    print(f"⏰ Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Test results tracking
    results = []
    
    # Test 1: Generate API Key
    api_key = test_generate_api_key()
    results.append(("generate_api_key", api_key is not None))
    
    # Test 2: Query endpoint
    query_success = test_query_endpoint(api_key)
    results.append(("query", query_success))
    
    # Test 3: Send endpoint
    send_success = test_send_endpoint(api_key)
    results.append(("send", send_success))
    
    # Summary
    print_section("Test Summary")
    total_tests = len(results)
    passed_tests = sum(1 for _, success in results if success)
    
    for endpoint, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {endpoint:<20} {status}")
    
    print(f"\n📊 Results: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! API documentation is working correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Check the API or documentation.")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 