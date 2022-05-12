#эффекты (Трансформы)
transform fall:
    anchor (0.0, 0.0) pos (0.0, 0.0)
    linear 0.1 pos (-50, 50)
    linear 0.1 pos (50, -50)
    linear 0.1 pos (50, 50)
    linear 0.1 pos (-50, -50)
    repeat
    
transform zoom_to(time=1, an_x=0.5, an_y=0.5, zoom_value=2):
    linear time zoom zoom_value anchor(an_x,an_y)

transform leap(dyz=0.01, dxz=0.005, dt=.4):
    yzoom 1.0
    easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
    easeout dt*0.25 yzoom 1.0 xzoom 1.0
    easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
    easeout dt*0.25 yzoom 1.0 xzoom 1.0