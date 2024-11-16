# Scene 14

Scene 14 recorded in the Solve4X dataset with 3 process instances.

Start: 2024-03-25 11:46:52  
End: 11:54:01 (0:07:08.766000)

This scene covers the following 3 process instances:


- [ID042](#id042): Defective asset return for repair
- [ID043](#id043): Asset repair
- [ID044](#id044): Self-service asset check-out

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A2, C1, C3  |
| Assets   | P1, P9, L3, K1  |



## ID042

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:46:58.473 | 11:47:03.332 | Enter room    | C1 | P1 | door |
| 2  | 11:47:14.361 | 11:47:26.010 | Describe quality issue    | A2, C1 | P1 | it_working_desk |
| 3  | 11:47:29.476 | 11:48:01.967 | Check asset quality    | A2 | P1 | it_working_desk |
| 4  | 11:48:05.597 | 11:48:35.908 | Check-In asset for repair    | A2 | P1 | it_working_desk |
| 5  | 11:48:40.280 | 11:48:45.260 | Move asset to repair desk    | A2 | P1 | repair_desk |
| 6  | 11:48:52.220 | 11:49:04.108 | Pick asset from warehouse    | A2 | P9 | mouse_cupboard |
| 7  | 11:49:08.617 | 11:49:33.479 | Check-Out asset to user    | A2 | P9 | it_working_desk |
| 8  | 11:49:36.659 | 11:49:43.505 | Handover asset to user    | A2, C1 | P9 | it_working_desk |
| 9  | 11:49:46.405 | 11:49:51.725 | Leave room    | C1 | P9 | door |

## ID043

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:50:08.745 | 11:50:48.978 | Carry out repair    | A2 | L3 | repair_desk |
| 2  | 11:50:50.471 | 11:51:29.087 | Chat    | A2, C3 |  |  |
| 3  | 11:51:31.174 | 11:51:48.625 | Carry out repair    | A2 | L3 | repair_desk |
| 4  | 11:51:50.566 | 11:53:22.618 | Check asset quality    | A2 | L3 | repair_desk |
| 5  | 11:53:36.643 | 11:53:49.166 | Update asset status in the system    | A2 | L3 | it_working_desk |
| 6  | 11:53:52.899 | 11:53:57.316 | Move asset to storage    | A2 | L3 | laptop_shelf |

## ID044

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:50:46.507 | 11:50:51.300 | Enter room    | C3 |  | door |
| 2  | 11:50:53.476 | 11:50:55.276 | Pick asset from self service desk    | C3 | K1 | self_service_storage |
| 3  | 11:50:55.590 | 11:51:29.217 | Chat    | A2, C3 |  |  |
| 4  | 11:51:31.769 | 11:51:36.196 | Leave room    | C3 | K1 | door |



## Scene Files

The files related to this scene are stored in `scene14/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene14.mp4`      |
| Video Log             | `scene14_vid.json` |
| Joined Scene OCEL[^1] | `scene14_ocel.json` |
| Video OCEL            | `scene14_video_ocel.json` |
| Ambient Sensor OCEL   | `scene14_sensors_ocel.json` |
| Motion Tracking       | `scene14_mov.csv`|
| Web Task Mining       | `scene14_ui.csv` |
| Reed Switches         | `scene14_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene14_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene14_temp_hum_sensor_window.csv` |

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
      "duration_ts": 6585856,
      "duration": "428.766667",
      "bit_rate": "1701299",
      "bits_per_raw_sample": "8",
      "nb_frames": "12863",
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
    "filename": "scene14.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "428.766667",
    "size": "91338969",
    "bit_rate": "1704217",
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