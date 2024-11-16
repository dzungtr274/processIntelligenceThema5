# Scene 11

Scene 11 recorded in the Solve4X dataset with 4 process instances.

Start: 2024-03-25 11:08:28  
End: 11:16:20 (0:07:52.200000)

This scene covers the following 4 process instances:


- [ID031](#id031): Defective asset return for repair
- [ID032](#id032): Asset repair
- [ID033](#id033): Self-service asset check-out
- [ID034](#id034): Self-service asset check-out

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A2, C3, C9  |
| Assets   | L1, L4, H5, H7  |



## ID031

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:08:33.666 | 11:08:37.107 | Enter room    | C3 | L1 | door |
| 2  | 11:08:39.511 | 11:09:04.973 | Describe quality issue    | C3, A2 | L1 | it_working_desk |
| 3  | 11:09:06.184 | 11:09:31.497 | Check asset quality    | A2 | L1 | it_working_desk |
| 4  | 11:09:34.706 | 11:10:32.784 | Check-In asset for repair    | A2 | L1 | it_working_desk |
| 5  | 11:10:33.922 | 11:10:41.148 | Move asset to repair desk    | A2 | L1 | repair_desk |
| 6  | 11:10:45.167 | 11:10:49.344 | Pick asset from warehouse    | A2 | L4 | laptop_shelf |
| 7  | 11:10:50.547 | 11:11:03.598 | Chat    | A2, C3 |  |  |
| 8  | 11:11:03.598 | 11:11:20.085 | Check asset quality    | A2 | L4 | it_working_desk |
| 9  | 11:11:22.001 | 11:11:45.494 | Check-Out asset to user    | A2 | L4 | it_working_desk |
| 10  | 11:11:45.743 | 11:11:52.791 | Handover asset to user    | A2, C3 | L4 | it_working_desk |
| 11  | 11:11:55.555 | 11:11:59.127 | Leave room    | C3 | L4 | door |

## ID032

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:12:11.966 | 11:13:39.627 | Carry out repair    | A2 | L1 | repair_desk |
| 2  | 11:13:41.473 | 11:13:50.938 | Chat    | A2, C3 |  |  |
| 3  | 11:13:51.388 | 11:14:14.152 | Carry out repair    | A2 | L1 | repair_desk |
| 4  | 11:14:19.210 | 11:14:29.883 | Check asset quality    | A2 | L1 | repair_desk |
| 5  | 11:14:31.067 | 11:14:48.748 | Chat    | A2, C9 |  |  |
| 6  | 11:14:50.601 | 11:15:08.611 | Check asset quality    | A2 | L1 | repair_desk |
| 7  | 11:15:20.505 | 11:16:05.985 | Update asset status in the system    | A2 | L1 | it_working_desk |
| 8  | 11:16:09.580 | 11:16:16.863 | Move asset to storage    | A2 | L1 | laptop_shelf |

## ID033

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:13:37.438 | 11:13:41.400 | Enter room    | C3 |  | door |
| 2  | 11:13:43.809 | 11:13:45.097 | Pick asset from self service desk    | C3 | H5 | self_service_storage |
| 3  | 11:13:45.307 | 11:13:50.457 | Chat    | A2, C3 |  |  |
| 4  | 11:13:51.193 | 11:13:54.724 | Leave room    | C3 | H5 | door |

## ID034

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:14:27.864 | 11:14:32.276 | Enter room    | C9 |  | door |
| 2  | 11:14:32.268 | 11:14:35.767 | Chat    | A2, C9 |  |  |
| 3  | 11:14:35.767 | 11:14:45.793 | Pick asset from self service desk    | C9 | H7 | self_service_storage |
| 4  | 11:14:47.545 | 11:14:51.710 | Leave room    | C9 | H7 | door |



## Scene Files

The files related to this scene are stored in `scene11/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene11.mp4`      |
| Video Log             | `scene11_vid.json` |
| Joined Scene OCEL[^1] | `scene11_ocel.json` |
| Video OCEL            | `scene11_video_ocel.json` |
| Ambient Sensor OCEL   | `scene11_sensors_ocel.json` |
| Motion Tracking       | `scene11_mov.csv`|
| Web Task Mining       | `scene11_ui.csv` |
| Reed Switches         | `scene11_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene11_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene11_temp_hum_sensor_window.csv` |

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
      "duration_ts": 7252992,
      "duration": "472.200000",
      "bit_rate": "1497322",
      "bits_per_raw_sample": "8",
      "nb_frames": "14166",
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
    "filename": "scene11.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "472.200000",
    "size": "88551457",
    "bit_rate": "1500236",
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