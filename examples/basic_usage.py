#!/usr/bin/env python3
"""
Basic usage example for quetzal-annotator package.

This example demonstrates how to:
1. Create a spectrum from peak data
2. Annotate the spectrum with a peptidoform
3. Examine the annotated spectrum
"""

import numpy as np
from quetzal_annotator import Spectrum, SpectrumAnnotator, ProformaPeptidoform

def main():
    # Example peak data (m/z and intensity pairs)
    mzs = np.array([147.1134, 175.1190, 204.1343, 232.1299, 261.1452, 289.1408, 
                    318.1561, 346.1517, 375.1670, 403.1626, 432.1779, 460.1735, 
                    489.1888, 517.1844, 546.1997, 574.1953, 603.2106, 631.2062, 
                    660.2215, 688.2171, 717.2324, 745.2280, 774.2433, 802.2389, 
                    831.2542, 859.2498, 888.2651, 916.2607, 945.2760, 973.2716])
    
    intensities = np.array([100.0, 45.2, 78.9, 23.1, 67.4, 12.8, 89.3, 34.7, 
                           56.1, 18.9, 72.6, 29.4, 81.2, 15.6, 63.8, 27.1, 
                           94.5, 41.3, 58.7, 22.4, 76.9, 33.8, 85.1, 19.7, 
                           69.4, 31.2, 91.8, 37.6, 52.9, 25.3])
    
    # Create a spectrum
    spectrum = Spectrum(mzs=mzs, intensities=intensities)
    
    # Set precursor information
    spectrum.precursor_mz = 1002.4567
    spectrum.charge = 2
    
    print(f"Spectrum created with {len(spectrum.mzs)} peaks")
    print(f"Precursor m/z: {spectrum.precursor_mz}")
    print(f"Charge: {spectrum.charge}")
    
    # Create a peptidoform using ProForma notation
    peptidoform = ProformaPeptidoform("PEPTIDE")
    
    print(f"\nPeptidoform: {peptidoform.sequence}")
    print(f"Theoretical m/z: {peptidoform.mz}")
    
    # Create annotator and annotate the spectrum
    annotator = SpectrumAnnotator()
    
    print("\nAnnotating spectrum...")
    annotated_spectrum = annotator.annotate(spectrum, peptidoform)
    
    # Print some annotation results
    print(f"\nAnnotation complete!")
    print(f"Number of annotated peaks: {len(annotated_spectrum.annotations)}")
    
    # Show some example annotations
    print("\nExample annotations:")
    for i, annotation in enumerate(annotated_spectrum.annotations[:5]):
        if annotation:
            print(f"  Peak {i+1} (m/z {spectrum.mzs[i]:.4f}): {annotation}")
    
    return annotated_spectrum

if __name__ == "__main__":
    main() 