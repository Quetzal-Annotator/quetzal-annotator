# Quetzal Annotator API Documentation

## Overview

The `quetzal-annotator` package provides comprehensive tools for annotating peptide fragment ion mass spectra using the PSI mzPAF standard. This document provides detailed API documentation for all major components.

## Installation

```bash
pip install quetzal_annotator
```

## Quick Start with USI

```python
import quetzal_annotator

# Define a Universal Spectrum Identifier for a spectrum deposited to ProteomeXchange
usi_string = 'mzspec:PXD015223:QExHF06277:scan:4202:HAEEQPTM[Oxidation]PR/2'

# Create a spectrum object and fetch a spectrum via a USI
spectrum = quetzal_annotator.Spectrum()
spectrum.fetch_spectrum(usi_string)

# Parse the USI string into an object and parse the peptidoform part
usi = quetzal_annotator.UniversalSpectrumIdentifier(usi_string)
peptidoform = quetzal_annotator.ProformaPeptidoform(usi.peptidoform_string)

# Annotate the spectrum
annotator = quetzal_annotator.SpectrumAnnotator()
annotator.annotate(spectrum, peptidoforms=[peptidoform], charges=[usi.charge])

# Display the results
print(f"Spectrum USI: {usi_string}")
print(spectrum.show())
```


## Quick Start with local peak data

```python
import quetzal_annotator

# Start with manually defined spectrum data
mzs = [102.0551, 129.1024, 147.1134, 175.1190, 204.1343, 227.1026, 518.7215, 727.1234, 810.3399]
intensities = [12.3, 87.5, 45.2, 100.0, 78.9, 54.8, 12.6, 2.1, 96.3]
precursor_mz = 1002.4567
charge = 2
proforma_string = 'PEPT[Phospho]IDER'

# Create a spectrum object and fill it with data
spectrum = quetzal_annotator.Spectrum()
spectrum.fill(mzs=mzs, intensities=intensities, precursor_mz=precursor_mz, charge_state=charge)

# Create a peptidoform object using ProForma notation
peptidoform = quetzal_annotator.ProformaPeptidoform(proforma_string)

# Annotate the spectrum
annotator = quetzal_annotator.SpectrumAnnotator()
annotator.annotate(spectrum, peptidoforms=[peptidoform], charges=[charge])

# Display the results
print(f"Spectrum annotated with {proforma_string} {charge}+")
print(spectrum.show())
```




## Core Classes

### Spectrum

The main class for representing mass spectrometry spectra.

```python
class Spectrum:
    def __init__(self, mzs: np.ndarray, intensities: np.ndarray, 
                 precursor_mz: float = None, charge: int = None)
```

**Parameters:**
- `mzs`: Array of m/z values (monotonically increasing)
- `intensities`: Array of intensity values
- `precursor_mz`: Precursor ion m/z value
- `charge`: Precursor ion charge state

**Attributes:**
- `mzs`: Array of m/z values
- `intensities`: Array of intensity values
- `precursor_mz`: Precursor ion m/z
- `charge`: Precursor ion charge
- `annotations`: List of peak annotations

### SpectrumAnnotator

Main class for annotating spectra with peptidoforms.

```python
class SpectrumAnnotator:
    def __init__(self, tolerance_ppm: float = 10.0)
    
    def annotate(self, spectrum: Spectrum, peptidoform: Peptidoform) -> Spectrum
```

**Parameters:**
- `tolerance_ppm`: Mass tolerance in parts per million for peak matching

**Methods:**
- `annotate()`: Annotates a spectrum with a peptidoform

### ProformaPeptidoform

Class for handling peptidoforms in ProForma notation.

```python
class ProformaPeptidoform:
    def __init__(self, sequence: str)
```

**Parameters:**
- `sequence`: ProForma sequence string

**Attributes:**
- `sequence`: The peptide sequence
- `mz`: Theoretical m/z value
- `mass`: Theoretical mass

### UniversalSpectrumIdentifier

Class for parsing and handling Universal Spectrum Identifiers (USI).

```python
class UniversalSpectrumIdentifier:
    def __init__(self, usi_string: str)
```

**Parameters:**
- `usi_string`: USI string to parse

**Attributes:**
- `dataset`: Dataset identifier
- `filename`: File name
- `scan`: Scan number
- `interpretation`: Peptide interpretation (if present)

### UniversalSpectrumIdentifierValidator

Class for validating USI strings.

```python
class UniversalSpectrumIdentifierValidator:
    def validate(self, usi: UniversalSpectrumIdentifier) -> bool
    def get_errors(self) -> List[str]
```

**Methods:**
- `validate()`: Returns True if USI is valid
- `get_errors()`: Returns list of validation errors

## Advanced Usage

### Spectrum Examination

```python
from quetzal_annotator import SpectrumExaminer

examiner = SpectrumExaminer()
results = examiner.examine(annotated_spectrum)
```

### Spectrum Comparison

```python
from quetzal_annotator import SpectrumComparator

comparator = SpectrumComparator()
similarity = comparator.compare(spectrum1, spectrum2)
```

### Ontology Handling

```python
from quetzal_annotator import Ontology, OntologyCollection

# Load PSI-MS ontology
ontology = Ontology("psi-ms.obo")
collection = OntologyCollection()
collection.add_ontology(ontology)
```

## Data Files

The package includes several important data files:

- `psi-ms.obo`: PSI-MS ontology in OBO format
- `psi-ms.json`: PSI-MS ontology in JSON format
- `unimod.obo`: UniMod modifications in OBO format
- `unimod.json`: UniMod modifications in JSON format
- `psi-mod.obo`: PSI-MOD ontology in OBO format
- `psi-mod.json`: PSI-MOD ontology in JSON format

These files are automatically included in the package and can be accessed programmatically.

## Error Handling

The package provides comprehensive error handling:

```python
try:
    spectrum = Spectrum(mzs, intensities)
    annotated = annotator.annotate(spectrum, peptidoform)
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Performance Considerations

- For large datasets, consider processing spectra in batches
- The annotation process is computationally intensive for complex peptidoforms
- USI validation is fast and can be used for real-time validation

## Contributing

Please refer to the main README for contribution guidelines and development setup instructions. 
