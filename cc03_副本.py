# 先查 PID
ps aux | grep DingTalk\ Helper

# 用 python 改 argv[0]（仅当前会话）
sudo python3 -c "
import ctypes, sys
lib = ctypes.CDLL('/usr/lib/libSystem.B.dylib')
lib.setproctitle(b'钉钉助手')
"