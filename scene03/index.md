# Scene 03

Scene 03 recorded in the Solve4X dataset with 4 process instances.

Start: 2024-03-25 09:06:07  
End: 09:18:47 (0:12:40)

This scene covers the following 4 process instances:


- [ID006](#id006): New asset inventory
- [ID007](#id007): Defective asset return for repair
- [ID008](#id008): Self-service asset check-out
- [ID009](#id009): Self-service asset check-out

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A1, C1, C5, C6  |
| Assets   | L5, L1, L3, K1, H4  |



## ID006

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:06:13.373 | 09:06:27.738 | Pick asset from warehouse    | A1 | L5 | laptop_shelf |
| 2  | 09:06:46.746 | 09:06:52.058 | Unpack asset    | A1 | L5 | repair_desk |
| 3  | 09:06:52.058 | 09:07:28.434 | Test asset quality and functionality    | A1 | L5 | repair_desk |
| 4  | 09:07:35.046 | 09:09:17.005 | Create system entry for asset    | A1 | L5 | it_working_desk |
| 5  | 09:09:21.264 | 09:09:45.179 | Install and configure asset    | A1 | L5 | repair_desk |
| 6  | 09:13:02.894 | 09:14:19.447 | Install and configure asset    | A1 | L5 | repair_desk |
| 7  | 09:14:49.390 | 09:16:01.112 | Install and configure asset    | A1 | L5 | repair_desk |
| 8  | 09:17:05.440 | 09:18:09.487 | Label asset    | A1 | L5 | repair_desk |
| 9  | 09:18:17.644 | 09:18:44.646 | Move asset to storage    | A1 | L5 | laptop_shelf |

## ID007

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:09:41.484 | 09:09:45.743 | Enter room    | C1 |  | door |
| 2  | 09:09:45.743 | 09:10:07.133 | Describe quality issue    | A1, C1 | L1 |  |
| 3  | 09:09:54.642 | 09:10:24.193 | Check asset quality    | A1 | L1 | it_working_desk |
| 4  | 09:10:38.015 | 09:11:10.822 | Check-In asset for repair    | A1 | L1 | it_working_desk |
| 5  | 09:11:15.130 | 09:11:21.338 | Move asset to repair desk    | A1 | L1 | repair_desk |
| 6  | 09:11:22.993 | 09:11:29.590 | Pick asset from warehouse    | A1 | L3 | laptop_shelf |
| 7  | 09:11:58.924 | 09:12:28.514 | Check-Out asset to user    | A1 | L3 | it_working_desk |
| 8  | 09:12:32.221 | 09:12:34.343 | Handover asset to user    | A1, C1 | L3 | it_working_desk |
| 9  | 09:12:38.600 | 09:12:43.132 | Leave room    | C1 |  | door |

## ID008

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:14:13.211 | 09:14:16.964 | Enter room    | C5 |  | door |
| 2  | 09:14:18.746 | 09:14:27.032 | Pick asset from self service desk    | C5 | K1 | self_service_storage |
| 3  | 09:14:47.597 | 09:14:53.222 | Leave room    | C5 |  | door |

## ID009

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:15:57.817 | 09:16:03.365 | Enter room    | C6 |  | door |
| 2  | 09:16:07.162 | 09:16:24.495 | Pick asset from self service desk    | C6 | H4 | self_service_storage |
| 3  | 09:17:03.867 | 09:17:09.673 | Leave room    | C6 |  | door |



## Scene Files

The files related to this scene are stored in `scene03/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene03.mp4`      |
| Video Log             | `scene03_vid.json` |
| Joined Scene OCEL[^1] | `scene03_ocel.json` |
| Video OCEL            | `scene03_video_ocel.json` |
| Ambient Sensor OCEL   | `scene03_sensors_ocel.json` |
| Motion Tracking       | `scene03_mov.csv`|
| Web Task Mining       | `scene03_ui.csv` |
| Reed Switches         | `scene03_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene03_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene03_temp_hum_sensor_window.csv` |

### Video file metrics

```json
{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
      "profile": "High",
      "codec_type": "video",
      "codec_tag_string": "avc1",
      "codec_tag": "0x31637661",
      "width": 1280,
      "height": 1440,
      "coded_width": 1280,
      "coded_height": 1440,
      "closed_captions": 0,
      "film_grain": 0,
      "has_b_frames": 2,
      "sample_aspect_ratio": "1:1",
      "display_aspect_ratio": "8:9",
      "pix_fmt": "yuv420p",
      "level": 40,
      "chroma_location": "left",
      "field_order": "progressive",
      "refs": 1,
      "is_avc": "true",
      "nal_length_size": "4",
      "id": "0x1",
      "r_frame_rate": "30/1",
      "avg_frame_rate": "30/1",
      "time_base": "1/15360",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 11676160,
      "duration": "760.166667",
      "bit_rate": "1421034",
      "bits_per_raw_sample": "8",
      "nb_frames": "22805",
      "extradata_size": 47,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "VideoHandler",
        "vendor_id": "[0][0][0][0]",
        "encoder": "Lavc60.31.102 libx264"
      }
    }
  ],
  "format": {
    "filename": "scene03.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "760.166667",
    "size": "135304082",
    "bit_rate": "1423941",
    "probe_score": 100,
    "tags": {
      "major_brand": "isom",
      "minor_version": "512",
      "compatible_brands": "isomiso2avc1mp41",
      "encoder": "Lavf60.16.100"
    }
  }
}
```

[^1]: OCEL is a standard designed to facilitate the exchange of object-centric event data across various case notions. 
The [OCEL website](www.ocel-standard.org) gives further information. 