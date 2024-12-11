import json
import os
from pathlib import Path


def merge_ocel_files(additional_file, input_folder, output_file):
    # Initialize the merged OCEL structure
    merged_ocel = {
        "ocel:global-event": {},
        "ocel:global-object": {},
        "ocel:global-log": {
            "ocel:attribute-names": set(),
            "ocel:object-types": set(),
            "ocel:version": None,
            "ocel:ordering": None,
        },
        "ocel:events": {},
        "ocel:objects": {},
    }

    additional_file_path = Path(additional_file)
    if additional_file_path.exists():
        with open(additional_file_path, 'r') as f:
            additional_ocel = json.load(f)

        # combine `ocel:global-log`
        merged_ocel["ocel:global-log"]["ocel:attribute-names"].update(
            additional_ocel["ocel:global-log"].get("ocel:attribute-names", [])
        )
        merged_ocel["ocel:global-log"]["ocel:object-types"].update(
            additional_ocel["ocel:global-log"].get("ocel:object-types", [])
        )
        if merged_ocel["ocel:global-log"]["ocel:version"] is None:
            merged_ocel["ocel:global-log"]["ocel:version"] = additional_ocel["ocel:global-log"].get("ocel:version")
        if merged_ocel["ocel:global-log"]["ocel:ordering"] is None:
            merged_ocel["ocel:global-log"]["ocel:ordering"] = additional_ocel["ocel:global-log"].get("ocel:ordering")

        # combine events and objects
        merged_ocel["ocel:events"].update(additional_ocel.get("ocel:events", {}))
        merged_ocel["ocel:objects"].update(additional_ocel.get("ocel:objects", {}))

    # Iterate over JSON files in the folder
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".jsonocel"):
                file_path = Path(root) / file
                with open(file_path, "r") as f:
                    ocel_data = json.load(f)
                
                # Merge `ocel:global-log`
                merged_ocel["ocel:global-log"]["ocel:attribute-names"].update(
                    ocel_data["ocel:global-log"].get("ocel:attribute-names", [])
                )
                merged_ocel["ocel:global-log"]["ocel:object-types"].update(
                    ocel_data["ocel:global-log"].get("ocel:object-types", [])
                )
                merged_ocel["ocel:global-log"]["ocel:version"] = ocel_data["ocel:global-log"].get("ocel:version")
                merged_ocel["ocel:global-log"]["ocel:ordering"] = ocel_data["ocel:global-log"].get("ocel:ordering")
                
                # Merge `ocel:events`
                merged_ocel["ocel:events"].update(ocel_data.get("ocel:events", {}))
                
                # Merge `ocel:objects`
                merged_ocel["ocel:objects"].update(ocel_data.get("ocel:objects", {}))

    sorted_events = dict(
        sorted(
            # use items to get key-value-relation
            merged_ocel["ocel:events"].items(),
            # [1] stands for the value
            key=lambda item: item[1].get("ocel:timestamp")
        )
    )

    merged_ocel["ocel:events"] = sorted_events

    # Convert sets back to lists for JSON compatibility
    merged_ocel["ocel:global-log"]["ocel:attribute-names"] = list(merged_ocel["ocel:global-log"]["ocel:attribute-names"])
    merged_ocel["ocel:global-log"]["ocel:object-types"] = list(merged_ocel["ocel:global-log"]["ocel:object-types"])

    # Save the merged OCEL to the output file
    with open(output_file, "w") as output_f:
        json.dump(merged_ocel, output_f, indent=4)

    print(f"Merged OCEL file saved to {output_file}")

# Paths for input folder and output file
additional_file_path = 'dataProcessing/filtered_itam_ocel.jsonocel'
input_folder_path = "dataProcessing/filteredSceneVideoOCEL/"  # Update to the folder containing your JSON files
output_file_path = "dataProcessing/itamSceneCombinedOCEL/itam_scene_combined_all.jsonocel"

merge_ocel_files(additional_file_path, input_folder_path, output_file_path)
