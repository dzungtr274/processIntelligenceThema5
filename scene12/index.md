# Scene 12

Scene 12 recorded in the Solve4X dataset with 4 process instances.

Start: 2024-03-25 11:19:40  
End: 11:27:56 (0:08:16.200000)

This scene covers the following 4 process instances:


- [ID035](#id035): Asset disbursement to clients
- [ID036](#id036): Asset disbursement to clients
- [ID037](#id037): Asset return
- [ID038](#id038): Asset return

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A2, C4, C5, C3, C9  |
| Assets   | M1, M2, H5, H7  |



## ID035

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:19:41.873 | 11:19:46.503 | Enter room    | C4 |  | door |
| 2  | 11:19:58.702 | 11:20:08.181 | Pick asset from warehouse    | A2 | M1 | monitor_storage |
| 3  | 11:20:10.905 | 11:20:31.799 | Check asset quality    | A2 | M1 | it_working_desk |
| 4  | 11:20:33.248 | 11:21:17.472 | Check-Out asset to user    | A2 | M1 | it_working_desk |
| 5  | 11:21:24.376 | 11:21:34.350 | Handover asset to user    | A2, C4 | M1 | it_working_desk |
| 6  | 11:21:49.245 | 11:21:56.733 | Leave room    | C4 | M1 | door |

## ID036

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:22:05.836 | 11:22:09.236 | Enter room    | C5 |  | door |
| 2  | 11:22:19.021 | 11:22:26.174 | Pick asset from warehouse    | A2 | M2 | monitor_storage |
| 3  | 11:22:27.285 | 11:22:47.214 | Check asset quality    | A2 | M2 | it_working_desk |
| 4  | 11:22:51.486 | 11:23:19.042 | Check-Out asset to user    | A2 | M2 | it_working_desk |
| 5  | 11:23:21.314 | 11:23:26.433 | Handover asset to user    | A2, C5 | M2 | it_working_desk |
| 6  | 11:23:29.040 | 11:23:34.241 | Leave room    | C5 | M2 | door |

## ID037

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:22:54.322 | 11:22:58.849 | Enter room    | C3 | H5 | door |
| 2  | 11:23:52.831 | 11:23:55.001 | Handover asset to admin    | A2, C3 | H5 | it_working_desk |
| 3  | 11:23:55.704 | 11:24:02.240 | Check asset quality    | A2 | H5 | it_working_desk |
| 4  | 11:24:00.319 | 11:24:05.103 | Leave room    | C3 |  | door |
| 5  | 11:24:03.984 | 11:26:36.805 | Check-In asset to storage    | A2 | H5 | it_working_desk |
| 6  | 11:26:37.756 | 11:26:44.703 | Move asset to storage    | A2 | H5 | self_service_storage |

## ID038

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:26:55.558 | 11:26:59.660 | Enter room    | C9 | H7 | door |
| 2  | 11:27:03.289 | 11:27:05.873 | Handover asset to admin    | A2, C9 | H7 | it_working_desk |
| 3  | 11:27:05.873 | 11:27:20.432 | Check asset quality    | A2 | H7 | it_working_desk |
| 4  | 11:27:22.158 | 11:27:27.694 | Leave room    | C9 |  | door |
| 5  | 11:27:24.744 | 11:27:47.066 | Check-In asset to storage    | A2 | H7 | it_working_desk |
| 6  | 11:27:47.506 | 11:27:53.633 | Move asset to storage    | A2 | H7 | self_service_storage |



## Scene Files

The files related to this scene are stored in `scene12/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene12.mp4`      |
| Video Log             | `scene12_vid.json` |
| Joined Scene OCEL[^1] | `scene12_ocel.json` |
| Video OCEL            | `scene12_video_ocel.json` |
| Ambient Sensor OCEL   | `scene12_sensors_ocel.json` |
| Motion Tracking       | `scene12_mov.csv`|
| Web Task Mining       | `scene12_ui.csv` |
| Reed Switches         | `scene12_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene12_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene12_temp_hum_sensor_window.csv` |

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
      "duration_ts": 7621632,
      "duration": "496.200000",
      "bit_rate": "1579955",
      "bits_per_raw_sample": "8",
      "nb_frames": "14886",
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
    "filename": "scene12.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "496.200000",
    "size": "98177510",
    "bit_rate": "1582869",
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