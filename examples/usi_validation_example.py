#!/usr/bin/env python3
"""
USI validation example for quetzal-annotator package.

This example demonstrates how to validate Universal Spectrum Identifiers (USI).
"""

from quetzal_annotator import UniversalSpectrumIdentifier, UniversalSpectrumIdentifierValidator

def main():
    # Create a validator
    validator = UniversalSpectrumIdentifierValidator()
    
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
            # Create USI object
            usi = UniversalSpectrumIdentifier(usi_string)
            
            # Validate
            is_valid = validator.validate(usi)
            
            if is_valid:
                print(f"  ✓ Valid USI")
                print(f"  Dataset: {usi.dataset}")
                print(f"  File: {usi.filename}")
                print(f"  Scan: {usi.scan}")
                if usi.interpretation:
                    print(f"  Interpretation: {usi.interpretation}")
            else:
                print(f"  ✗ Invalid USI")
                print(f"  Errors: {validator.get_errors()}")
                
        except Exception as e:
            print(f"  ✗ Error parsing USI: {e}")
    
    print("\n" + "=" * 50)
    print("Validation complete!")

if __name__ == "__main__":
    main() 