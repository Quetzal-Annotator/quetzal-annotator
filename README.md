# quetzal-annotator
Quetzal is a peptide fragment ion spectrum annotation tool to assist researchers in annotating and examining tandem mass spectra to ensure that they correctly support study conclusions. Quetzal annotates spectra using the new Human Proteome Organization ([HUPO](https://hupo.org/)) Proteomics Standards Initiative ([PSI](https://psidev.info/)) [mzPAF](https://psidev.info/mzPAF/) standard for fragment ion peak annotation. Quetzal includes a Python-based codebase, a web-service endpoint that provides annotation services, and a user-friendly web-based application for annotating spectra and producing publication-quality figures. 

# Using the Web Interface
The public web interface for *Quetzal* can be accessed at https://proteomecentral.proteomexchange.org/quetzal/

The page is divided into four main sections (_Import_, _Edit_, _Explore_, _Export_), another with general "About" information and links, and one for viewing debug information.

## Import
This is where a spectrum is entered into *Quetzal*.  Data can be fetched via a [Universal Spectrum Identifier](https://www.psidev.info/usi) (**USI**), or entered as a **peak list**.

A **USI** is not required to have an interpretation; in this case only basic annotation will be performed by *Quetzal*. The user can also specify which of the *PROXI* repositories to fetch spectrum data from, including private password-protected data in *PRIDE*.  For the latter, you will be prompted for your credentials, which will be used until the *Log Out* button is pressed, or the browser tab is closed.
>[!TIP]
>Not all datasets are hosted by all providers, and even portions of a given dataset may be missing for a given provider.
>Also, some providers furnish different levels of metadata.

A **peak list** consists of rows with at least two columns (*m/z* and *intensity*), with an optional third column containing peak annotations.  Columns can be separated by one or more space characters (including combinations, e.g. tabs and spaces), and empty values are not allowed. The list can either be typed/pasted into the text box, or a file of the proper format can be dragged and dropped into the same box.
Other than peaks (and optional annotations), *Quetzal* also recognizes the following special keywords when importing via the peak list mechanism: `PRECURSORMZ`, `PEPTIDOFORMS`, `CHARGES`, `m/z`, `Peptide`, and `Charge`.  If any of these strings is present as the first column in a given line of text, the value is taken from the second column.
>[!TIP]
>When using the *Download TSV* function, the file generated contains these values (and annotations), and is thus readily importable back into *Quetzal*

Once the **USI** or **peak list** has been entered, click on the corresponding button to import the data and run the annotator. If successful, the page will switch to the _Explore_ section.

### Import via direct link
External applications may link to *Quetzal* with the optional `usi` and `provider` URL parameters. If `usi` is detected, the data will be fetched (from `provider`, if specified) and automatically annotated.

## Edit
Once a spectrum has been loaded into _Quetzal_, this section allows the user to add or modify spectrum properties such as precursor m/z and charge, as well as the peptidoform. Editing the latter can be useful when testing alternate interpretations of a particular spectrum, and must follow the [PSI ProForma notation](https://github.com/HUPO-PSI/ProForma) (a pop-up window has a few simple syntax examples).  The annotator parameters of fragmentation type, isobaric labeling, and m/z tolerance for matching ions can also be set here.
>[!TIP]
>HCD and CID consider only _a/b/y_ backbone ions, ETD considers only _c/z_, while EThcD considers them all.

The lower pane displays the current annotations, and allows the user to edit them individually.  While _Quetzal_ follows the [PSI mzPAF](https://github.com/HUPO-PSI/mzPAF) format, the user is free to type any text (or none) when annotating peaks.

### User Feedback
To send an alternate interpretation and/or provide feedback on one or a few peaks, the user may edit that peak's annotation using the form, adding the string "**Comment:**" anywhere in the annotation, and choose to **Save Annotations**. This will trigger a manual review mechanism on our part.  An email address may be included in the comment for further engagement; submissions are anonymous otherwise.
>[!TIP]
Note that you will need to re-edit the annotation to remove the Comment and attached report before generating an image.

Users are also encouraged to file GitHub issues for more complex items or to report observed shortcomings with the annotator and/or user interface (link in toolbar at top pf page, need a GitHub account).

## Explore
This section features an interactive annotated spectrum, along with a matched ion table, basic ion statistics, and full annotated peak list.

The top left corner of the **MS/MS spectrum** shows the experimental _m/z_, the calculated _peptidoform m/z_, and the difference in parts per million (ppm).  The spectrum can be zoomed and panned (in either/both X/Y axes) to potentially reveal smaller peaks and extra annotations that are otherwise hidden to avoid overcrowding the display.  For convenience, most of these features are accessible both via mouse gestures and page controls.  The _Reset Zoom_ button reverts the view to the original (full) scale.

The **matched Ion Series table** highlights those positions where an ion has been detected; bright colors indicate detection of the main (backbone) ion, whereas a darker shade indicates detection only via a neutral loss (e.g. H2O loss from a backbone ion).  Amino acids or terminii with mass modifications are highlighted in yellow.

Below that, the **Peak Annotations table** provides comprehensive data on each peak in the spectrum: _m/z_; intensity, both _raw_ and _normalized_ (where 100.0 corresponds to the highest intensity peak, along with a light green shaded bar); and a highlighted _ion type_.  The ion types, in order from left to right, are: backbone **a**/**b**/**c**/**x**/**y**/**z**, **I**mmonium, **prec**ursor, isobaric **rep**orter, **int**ernal fragment, **mol**ecular formula, unknown (**?**), and those identified to a molecule **other** than the identified peptidoform.  The bottom of the table shows the share of the total intensity ascribed to each of the ion types.  This information is also available graphically by clicking on the _Ion Stats_ link at the top right of this table.  A _mass defect_ plot is also available.

>[!TIP]
>The ion annotation color scheme is preserved across the various views, so that all data associated with _e.g._ a y-ion is always shown in red.

## Export
This section enables the production of publication-quality figures, as well as text output of the annotated spectrum.

The _Preview_ button displays the image on the page just as it would be generated, and thus allows the user to test various configurations and settings before final download; a custom figure legend is also displayed below. There are options for downloading a Scalable Vector Graphics (**SVG**) or Portable Document Format (**PDF**) file, both of which are inherently resolution-agnostic and thus will not suffer from pixelation effects.  The former can easily be imported or included in various media, such as web pages, _Word_ documents, _PowerPoint_ slides, etc; the latter is more apt as a single-page document that may be compiled as e.g. supplementary material.

Other than the min/max m/z range, y max (where 100 = most intense peak), and min intensity to label a peak, there are output options to hide/display the following elements:
![image](https://github.com/user-attachments/assets/8290e67c-0af3-4282-81e8-6bc4f4276491)

## Log / Errors
This section contains detailed messages reported by the application, which can be useful for debugging or reporting issues.


# Public API
*Quetzal* can be used to annotate MS/MS spectra programmatically via a publicly available web service endpoint, which enables external tools to integrate its powerful annotation algorithm as well as publication-quality figures, be it from another web interface, desktop application, command-line script, etc.

Requests must be made as a *POST* _http_ query to https://proteomecentral.proteomexchange.org/api/proxi/v0.1/annotate?resultType=full&tolerance=10 . The _tolerance_ value, expressed in parts per million (ppm, with default=10), restricts peak matching to a window of this width; a large enough value (e.g. 500) is recommended for low-resolution data, such as from old ion trap instruments. Input and output are *JSON* objects described below.

## Input
The input payload object closely follows the [PROXI](https://github.com/HUPO-PSI/proxi-schemas/blob/master/specs/proxi-specifications.adoc) specification; the outline of its structure is:

    [
      {
        "mzs": [],
        "intensities": [],
        "attributes": [],
        "usi": "",
        "interpretations": [],
        "extended_data": {}
      }
    ]
**Note**: the payload object is an array, where each element represents a single spectrum to be annotated. Multiple spectra can thus be annotated in one request.

### Spectrum Data
The minimum information required for annotation is the MS/MS spectrum data, represented as an array of ***mzs*** with *monotonically increasing* values, and corresponding ***intensities***. Both arrays are required, must be of the same size and contain *float* values.

### Metadata
Spectrum information such as scan number, charge state, etc, as well as identification information is provided under the ***attributes*** array, where each object has the basic format:

       {
         "accession": "",
         "name": "",
         "value": ""
        }
Each element's  ***accession*** and ***name*** refer to an entry in the [PSI MS Ontology](https://www.ebi.ac.uk/ols4/ontologies/ms), and the ***value*** type should match the one in the schema.

While all *attributes* are optional, some are required for most aspects of the annotation to work.
|accession|name|type|purpose|
|--|--|--|--|
|MS:1003169|proforma peptidoform sequence|[PSI Proforma](https://github.com/HUPO-PSI/ProForma) string|annotate fragmentation ion peaks
|MS:1000744|selected ion m/z|float|annotate precursor peaks; calculate m/z difference vs. theoretical|
|MS:1000827|isolation window target m/z|float|annotate precursor peaks; calculate m/z difference vs. theoretical|
|MS:1000828|isolation window lower offset|float|annotate precursor peaks|
|MS:1000829|isolation window upper offset|float|(same as above)|
|MS:1000041|charge state|integer|(same as above)|
|MS:1000512|filter string|string|may control ion series considered for annotation if dissociation type can be extracted (e.g. *c/z* ions for ETD, etc)|
|MS:1003061|spectrum name|string|potentially used in image title|

The optional ***usi*** string can be specified for spectra for which a [Universal Spectrum Identifier](https://www.psidev.info/usi) is known; it is simply used as a title in the output image.

### Peak interpretations
The ***interpretations*** array holds annotations for each peak in the spectrum; as such, and when present, it should be the same size as the *mzs* and *intensities* arrays. The value of this array is ignored unless the _skip_annotation_ user parameter is set to `true` (see below), in which case no further annotation is undertaken.

The annotations generated by *Quetzal* are in [mzPAF](https://github.com/HUPO-PSI/mzPAF), but when pre-filled by the client they can be any string.  This can be useful when the user wants to override the _Quetzal_ annotation of one or more peaks in favor of a custom one for use in the final image.

### Extended data
The optional ***extended_data*** element may contain the  ***user_parameters*** object, which can be used to control certain aspects of the spectrum processing and output.  Crucially, it is required when requesting an image, and has the following potential attributes (all are optional):
|parameter|type|purpose|
|--|--|--|
|dissociation_type|string, one of [HCD, CID, ETD, EThcD]|Override inferred value used to annotate fragments|
|isobaric_labeling_mode|string, one of [automatic, TMT, iTRAQ, none]|(same as above)|
|skip_annotation|boolean|if `true`, use provided _interpretations_|
|create_svg|boolean|generate SVG image|
|create_pdf|boolean|generate PDF image|
|show_usi|boolean|image output option (see graphic in _Export_ section)|
|show_sequence|boolean|(same as above)|
|show_b_and_y_flags|boolean|(same as above)|
|show_coverage_table|boolean|(same as above)|
|show_precursor_mzs|boolean|(same as above)|
|show_mass_deltas|boolean|(same as above)|
|label_internal_fragments|boolean|(same as above)|
|label_unknown_peaks|boolean|(same as above)|
|label_neutral_losses|boolean|(same as above)|

## Output
The response object contains two elements: an ***annotated_spectra*** array, and a ***status*** object.

### Status
The contents of the *status* object should be examined, as they contain potential issues encountered during processing; it has the following structure:

    {
      "status": "",
      "status_code": <N>,
      "description": "",
      "log": []
    }

***status*** and ***status_code*** follow the [standard HTTP protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) (e.g. "OK" / 200, etc).  ***description*** contains a more verbose, user-friendly summary of the status.  The ***log*** array is a series of strings that detail the processing steps and actions taken during annotation and image generation; it is mostly useful for debugging.

### Annotated Spectra
The ***annotated_spectra*** array is equivalent to the input payload array (basic object structure described above), but with certain portions augmented in part or in full.  The list below is focused only on the potential changes made after calling _Quetzal_.

#### Peak interpretations and spectrum data
As noted above, the ***interpretations*** array holds annotations for each peak in the spectrum, and will contain newly-computed _mzPAF_ annotations unless _skip_annotation_ was set to `true` in the request.  Of note, _Quetzal_ **will not annotate zero-intensity peaks, and will remove those peaks from the spectrum**.  Therefore, there is a potential for the **_mzs_** and **_intensities_** arrays returned to be different than what was in the input payload, and thus it is recommended to update the spectrum data with these new arrays.

#### Extended data and images
The ***extended_data*** object may contain one or more of the following new elements:  _**svg**_, _**pdf**_, _**figure_legend**_, **_inferred_attributes_**, and _**metrics**_.

If an image was requested, the serialized data will be contained in _svg_ and/or _pdf_, alongside a custom _figure_legend_ that may be used as a figure caption.

The _inferred_attributes_ object may contain some of the following elements:
|element|type|purpose|
|--|--|--|
|used dissociation type|string, one of [HCD, CID, ETD, EThcD]|type used when annotating ion series|
|used isobaric labeling mode|string, one of [automatic, TMT, iTRAQ, none]|mode used when annotating ion series|
|filter string inferred dissociation type|(same as above)|inefrred type from _filter string_ attribute, if provided in payload|

The _metrics_ object contains some trace and debug data; it is not recommended for use at the moment.
