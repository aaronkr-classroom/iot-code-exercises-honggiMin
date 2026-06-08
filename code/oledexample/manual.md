# animation for 64*48 OLED 
**This is not a evaluation item. This just made for fun**

This code uses the lib file from [esp32-iotmakr-main](https://github.com/aaronkr-courses/esp32-iotmaker/tree/main/micropython)
<br>[gif to cpp site](https://huykhong.com/IOT/gif2cpp/)(Get only the array) 

This program uses a 64*48 array to output OLED.
<br>Since each array is one-dimensional, it may appear distorted on screens of different sizes.

The animation repeats the output of the array.
<br>If you want to use a different animation, you must use a byte array of 384 bytes (64*48).
    
>line 18

    raw_frames = [
    bytearray([])
    ]

If the screen is distorted even though the array size is correct, try changing the alignment method from HLSB to HMSB or VLSB.
<br>The OLED I used displayed the HLSB method correctly.

>line 438

    fb_list = [framebuf.FrameBuffer(data, WIDTH, HEIGHT, framebuf.MONO_HLSB) for data in raw_frames]

If you want to adjust the frames per second, please adjust this variable.

>line 442

    FRAME_DELAY_MS = 50
