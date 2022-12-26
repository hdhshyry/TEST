from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
devices =AudioUtilities.GetSpeakers()
Interface =devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(Interface, POINTER(IAudioEndpointVolume))
volume.SetMute(0,None)
current=volume.GetMasterVolumeLevel()
print(devices)