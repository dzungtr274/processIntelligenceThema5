# Scene 06

Scene 06 recorded in the Solve4X dataset with 4 process instances.

Start: 2024-03-25 09:29:43  
End: 09:36:55 (0:07:12)

This scene covers the following 4 process instances:


- [ID015](#id015): New asset inventory
- [ID016](#id016): Self-service asset check-out
- [ID017](#id017): Asset return
- [ID018](#id018): Self-service asset check-out

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A1, C10, C1, C9  |
| Assets   | L6, H11, L3, P2, K4  |



## ID015

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:30:02.613 | 09:30:08.469 | Pick asset from warehouse    | A1 | L6 | laptop_shelf |
| 2  | 09:30:15.016 | 09:30:26.491 | Unpack asset    | A1 | L6 | repair_desk |
| 3  | 09:30:26.491 | 09:30:40.459 | Test asset quality and functionality    | A1 | L6 | repair_desk |
| 4  | 09:30:52.778 | 09:31:00.084 | Install and configure asset    | A1 | L6 | repair_desk |
| 5  | 09:31:57.081 | 09:32:16.057 | Install and configure asset    | A1 | L6 | repair_desk |
| 6  | 09:32:19.153 | 09:32:50.008 | Label asset    | A1 | L6 | repair_desk |
| 7  | 09:33:21.003 | 09:34:11.037 | Create system entry for asset    | A1 | L6 | it_working_desk |
| 8  | 09:34:43.043 | 09:34:48.870 | Move asset to storage    | A1 | L6 | laptop_shelf |

## ID016

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:30:55.103 | 09:30:59.847 | Enter room    | C10 |  | door |
| 2  | 09:31:15.275 | 09:31:50.275 | Pick asset from self service desk    | C10 | H11 | self_service_storage |
| 3  | 09:31:51.974 | 09:31:57.974 | Leave room    | C10 |  | door |

## ID017

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:32:58.639 | 09:33:07.155 | Enter room    | C1 |  | door |
| 2  | 09:34:53.139 | 09:35:04.139 | Handover asset to admin    | A1, C1 | L3, P2 | it_working_desk |
| 3  | 09:35:04.139 | 09:35:46.139 | Check asset quality    | A1 | L3, P2 | it_working_desk |
| 4  | 09:35:54.139 | 09:36:28.139 | Check-In asset to storage    | A1 | L3, P2 | it_working_desk |
| 5  | 09:35:52.643 | 09:36:00.643 | Leave room    | C1 |  | door |
| 6  | 09:36:37.086 | 09:36:42.086 | Move asset to storage    | A1 | L3 | laptop_shelf |
| 7  | 09:36:37.139 | 09:36:50.086 | Move asset to storage    | A1 | P2 | mouse_cupboard |

## ID018

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:36:37.712 | 09:36:40.712 | Enter room    | C9 |  | door |
| 2  | 09:36:40.712 | 09:36:43.712 | Pick asset from self service desk    | C9 | K4 | self_service_storage |
| 3  | 09:36:43.712 | 09:36:48.712 | Leave room    | C9 |  | door |



## Scene Files

The files related to this scene are stored in `scene06/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene06.mp4`      |
| Video Log             | `scene06_vid.json` |
| Joined Scene OCEL[^1] | `scene06_ocel.json` |
| Video OCEL            | `scene06_video_ocel.json` |
| Ambient Sensor OCEL   | `scene06_sensors_ocel.json` |
| Motion Tracking       | `scene06_mov.csv`|
| Web Task Mining       | `scene06_ui.csv` |
| Reed Switches         | `scene06_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene06_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene06_temp_hum_sensor_window.csv` |

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
      "duration_ts": 6638592,
      "duration": "432.200000",
      "bit_rate": "1586427",
      "bits_per_raw_sample": "8",
      "nb_frames": "12966",
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
    "filename": "scene06.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "432.200000",
    "size": "85864301",
    "bit_rate": "1589343",
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