#!/usr/bin/env python3
"""
Test script to verify Odoo authentication
"""

import xmlrpc.client
import os
import json

def load_config():
    """Load configuration from file or environment variables"""
    # Try environment variables first
    if all(var in os.environ for var in ["ODOO_URL", "ODOO_DB", "ODOO_USERNAME", "ODOO_PASSWORD"]):
        return {
            "url": os.environ["ODOO_URL"],
            "db": os.environ["ODOO_DB"],
            "username": os.environ["ODOO_USERNAME"],
            "password": os.environ["ODOO_PASSWORD"],
        }
    
    # Try config file
    config_paths = [
        "./odoo_config.json",
        os.path.expanduser("~/.config/odoo/config.json"),
        os.path.expanduser("~/.odoo_config.json"),
    ]
    
    for path in config_paths:
        expanded_path = os.path.expanduser(path)
        if os.path.exists(expanded_path):
            with open(expanded_path, "r") as f:
                return json.load(f)
    
    raise FileNotFoundError("No Odoo configuration found")

def test_authentication():
    """Test Odoo authentication"""
    config = load_config()
    
    print(f"Testing Odoo authentication:")
    print(f"  URL: {config['url']}")
    print(f"  Database: {config['db']}")
    print(f"  Username: {config['username']}")
    
    try:
        # Create XML-RPC connection
        common = xmlrpc.client.ServerProxy(f"{config['url']}/xmlrpc/2/common")
        print(f"Connected to XML-RPC common endpoint")
        
        # Test authentication
        print("Attempting authentication...")
        uid = common.authenticate(config['db'], config['username'], config['password'], {})
        
        if uid:
            print(f"✅ Authentication successful! UID: {uid}")
            
            # Test models endpoint
            models = xmlrpc.client.ServerProxy(f"{config['url']}/xmlrpc/2/object")
            # Test a simple method
            try:
                model_list = models.execute_kw(config['db'], uid, config['password'], 'ir.model', 'search', [[]])
                print(f"✅ Models endpoint working. Found {len(model_list)} models")
                return True
            except Exception as e:
                print(f"❌ Models endpoint test failed: {e}")
                return False
        else:
            print("❌ Authentication failed: Invalid credentials")
            return False
            
    except Exception as e:
        print(f"❌ Authentication failed with error: {e}")
        return False

if __name__ == "__main__":
    test_authentication()
