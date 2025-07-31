#!/usr/bin/env python3
"""
Basic usage example for quetzal-annotator package.

This example demonstrates how to:
1. Create a spectrum from peak data
2. Annotate the spectrum with a peptidoform
3. Examine the annotated spectrum
"""

from quetzal_annotator import Spectrum, SpectrumAnnotator, ProformaPeptidoform

def main():
    # Example peak data (m/z and intensity pairs)
    mzs = [ 147.1134, 175.1190, 204.1343, 232.1299, 261.1452, 289.1408, 
            318.1561, 346.1517, 375.1670, 403.1626, 432.1779, 460.1735, 
            489.1888, 517.1844, 546.1997, 574.1953, 603.2106, 631.2062, 
            660.2215, 688.2171, 717.2324, 745.2280, 774.2433, 802.2389, 
            831.2542, 859.2498, 888.2651, 916.2607, 945.2760, 973.2716 ]
    
    intensities = [ 100.0, 45.2, 78.9, 23.1, 67.4, 12.8, 89.3, 34.7, 
                    56.1, 18.9, 72.6, 29.4, 81.2, 15.6, 63.8, 27.1, 
                    94.5, 41.3, 58.7, 22.4, 76.9, 33.8, 85.1, 19.7, 
                    69.4, 31.2, 91.8, 37.6, 52.9, 25.3 ]

    charge = 2
    precursor_mz = 1002.4567
    peptidoform_string = 'PEPT[Phospho]IDE'

    # Create a spectrum and fill it with the available data
    spectrum = Spectrum()
    spectrum.fill(mzs=mzs, intensities=intensities, precursor_mz=precursor_mz, charge_state=charge)

    print(f"Spectrum created with {spectrum.attributes['number of peaks']} peaks")
    print(f"Precursor m/z: {spectrum.analytes['1']['precursor_mz']}")
    print(f"Charge: {spectrum.analytes['1']['charge state']}")
    
    # Create a peptidoform using ProForma notation
    peptidoform = ProformaPeptidoform(peptidoform_string)
    
    print(f"Peptidoform: {peptidoform.peptidoform_string}")
    print(f"Neutral mass: {peptidoform.neutral_mass}")
    
    # Create annotator and annotate the spectrum
    annotator = SpectrumAnnotator()
    
    print("Annotating spectrum...")
    annotator.annotate(spectrum, peptidoforms=[peptidoform], charges=[charge])
    
    # Print some annotation results
    print(f"Annotation complete!")
    
    # Show some example annotations
    print("Example annotations:")
    for i, peak in enumerate(spectrum.peak_list):
        i_peak, mz, intensity, annotation = peak[0:4]
        if annotation != '?':
            print(f"  Peak {i+1} (m/z {mz:.4f}): {annotation}")
    
    return spectrum

if __name__ == "__main__":
    main() 