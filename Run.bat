@Echo off
title ETHChecker Atomic Mmdrza.Com
Pushd "%~dp0"
:loop
python EthAtomCheckOnlineNoAPI.py
goto loop
