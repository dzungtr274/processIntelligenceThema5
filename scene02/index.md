# Scene 02

Scene 02 recorded in the Solve4X dataset with 2 process instances.

Start: 2024-03-25 08:57:06  
End: 09:00:47 (0:03:41)

This scene covers the following 2 process instances:


- [ID004](#id004): New asset inventory
- [ID005](#id005): New asset inventory

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A1  |
| Assets   | P1, K1  |



## ID004

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 08:57:06.000 | 08:57:17.430 | Pick asset from warehouse    | A1 | P1 | mouse_cupboard |
| 2  | 08:57:17.430 | 08:57:20.422 | Unpack asset    | A1 | P1 | it_working_desk |
| 3  | 08:57:20.422 | 08:57:37.127 | Test asset quality and functionality    | A1 | P1 | it_working_desk |
| 4  | 08:57:20.422 | 08:57:37.127 | Install and configure asset    | A1 | P1 | it_working_desk |
| 5  | 08:57:47.169 | 08:58:35.078 | Create system entry for asset    | A1 | P1 | it_working_desk |
| 6  | 08:58:36.221 | 08:58:42.325 | Move asset to storage    | A1 | P1 | mouse_cupboard |

## ID005

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 08:58:50.685 | 08:58:53.830 | Pick asset from self service desk    | A1 | K1 | self_service_storage |
| 2  | 08:58:53.830 | 08:59:10.237 | Unpack asset    | A1 | K1 | it_working_desk |
| 3  | 08:59:10.237 | 08:59:22.404 | Test asset quality and functionality    | A1 | K1 | it_working_desk |
| 4  | 08:59:22.404 | 08:59:53.100 | Install and configure asset    | A1 | K1 | it_working_desk |
| 5  | 09:00:13.303 | 09:00:32.247 | Create system entry for asset    | A1 | K1 | it_working_desk |
| 6  | 09:00:33.980 | 09:00:39.047 | Move asset to storage    | A1 | K1 | self_service_storage |



## Scene Files

The files related to this scene are stored in `scene02/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene02.mp4`      |
| Video Log             | `scene02_vid.json` |
| Joined Scene OCEL[^1] | `scene02_ocel.json` |
| Video OCEL            | `scene02_video_ocel.json` |
| Ambient Sensor OCEL   | `scene02_sensors_ocel.json` |
| Motion Tracking       | `scene02_mov.csv`|
| Web Task Mining       | `scene02_ui.csv` |
| Reed Switches         | `scene02_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene02_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene02_temp_hum_sensor_window.csv` |

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
      "duration_ts": 3389952,
      "duration": "220.700000",
      "bit_rate": "1736090",
      "bits_per_raw_sample": "8",
      "nb_frames": "6621",
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
    "filename": "scene02.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "220.700000",
    "size": "47975361",
    "bit_rate": "1739025",
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