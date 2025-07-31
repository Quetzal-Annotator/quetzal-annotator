#!/usr/bin/env python3
"""
USI validation example for quetzal-annotator package.

This example demonstrates how to validate Universal Spectrum Identifiers (USI).
"""

import quetzal_annotator

def main():
    
    # Example USIs to test
    test_usis = [
        "mzspec:PXD000561:Adult_Frontalcortex_bRP_Elite_85_f09:scan:17555:VLHPLEGAVVIIFK/2",
        "mzspec:MSV000079514:Adult_Frontalcortex_bRP_Elite_85_f09:scan:17555:VLHPLEGAVVIIFK/2",
        "mzspec:PXD000561:Adult_Frontalcortex_bRP_Elite_85_f09:scan:17555",
        "invalid:usi:format",
        "mzspec:PXD000561:Adult_Frontalcortex_bRP_Elite_85_f09:scan:17555:VLHPLEGAVVIIFK/",
        "mzspec:PXD000561:Adult_Frontalcortex_bRP_Elite_85_f09:scan:17555:VLHPLEGAVVIIFK/0"
    ]
    
    print("USI Validation Examples")
    print("=" * 50)
    
    for usi_string in test_usis:
        print(f"\nTesting USI: {usi_string}")
        
        try:
            # Create USI object by parsing the supplied input USI string
            usi = quetzal_annotator.UniversalSpectrumIdentifier(usi_string)
            
            if usi.is_valid:
                print(f"  ✓ Valid USI")
                print(f"  Dataset: {usi.collection_identifier}")
                print(f"  File: {usi.ms_run_name}")
                print(f"  Scan: {usi.index}")
                if usi.interpretation:
                    print(f"  Interpretation: {usi.interpretation}")
            else:
                print(f"  ✗ Invalid USI")
                print(f"  Errors: {usi.error_code}: {usi.error_message}")
                
        except Exception as e:
            print(f"  ✗ Error parsing USI: {e}")
    
    print("\n" + "=" * 50)
    print("Validation complete!")

if __name__ == "__main__":
    main() 