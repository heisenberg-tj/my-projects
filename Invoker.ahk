; =====================================================================
; ArcaneKael v111.0 - Strict Orbs Lock (Tab, Caps, X) & TRUE INSTANT MODE
; AutoHotkey v1.1 - PURE INPUT 0ms - 100% NO MOUSE FREEZE
; =====================================================================
#NoEnv
#Persistent
#SingleInstance Force
#KeyHistory 0
#UseHook On 
ListLines Off
Process, Priority,, High 
SendMode Input
SetBatchLines, -1

global IsCasting := 0

if !A_IsAdmin
{
    Run *RunAs "%A_ScriptFullPath%"
    ExitApp
}

$F3::
Suspend, Toggle
if (A_IsSuspended)
    ToolTip, OFF - Kael Sleep, 1, 1
else
    ToolTip, ON - Kael Active, 1, 1
SetTimer, RemoveToolTip, -1200
return

RemoveToolTip:
ToolTip
return

; --- БЫСТРЫЙ И БЕЗОПАСНЫЙ КЛИКЕР НА N ---
#If WinActive("ahk_exe war3.exe") && !A_IsSuspended
$n::
While GetKeyState("n", "P")
{
    SendInput {LButton}
    DllCall("Sleep", "UInt", 30)
}
return
#If

; =====================================================================
; БЛОКИРОВКА ТОЛЬКО СФЕР ВО ВРЕМЯ КАСТА
; =====================================================================
#If WinActive("ahk_exe war3.exe") && (IsCasting = 1)
$Tab::      return
$CapsLock:: return
$x::        return
#If

; =====================================================================
; НАБОР №1 (БЕЗ SHIFT — 0 МС)
; =====================================================================
#If WinActive("ahk_exe war3.exe") && !A_IsSuspended && !GetKeyState("Shift", "P")
$g:: ; Ghost Walk (QQWR)
    InstantCast("{Blind}{vk51 2}{vk57}{vk52}")
    KeyWait, g
return
$y:: ; Cold Snap (QQQR)
    InstantCast("{Blind}{vk51 3}{vk52}")
    KeyWait, y
return
$f:: ; Ice Wall (QQER)
    InstantCast("{Blind}{vk51 2}{vk45}{vk52}")
    KeyWait, f
return
$b:: ; EMP (WWWR)
    InstantCast("{Blind}{vk57 3}{vk52}")
    KeyWait, b
return
$w:: ; Tornado (WWQR)
    InstantCast("{Blind}{vk57 2}{vk51}{vk52}")
    KeyWait, w
return
$e:: ; Sun Strike (EEER)
    InstantCast("{Blind}{vk45 3}{vk52}")
    KeyWait, e
return
$q:: ; Chaos Meteor (EEWR)
    InstantCast("{Blind}{vk45 2}{vk57}{vk52}")
    KeyWait, q
return
$v:: ; Deafening Blast (QWER)
    InstantCast("{Blind}{vk51}{vk57}{vk45}{vk52}")
    KeyWait, v
return
$r:: ; Forge Spirit (EEQR)
    InstantCast("{Blind}{vk45 2}{vk51}{vk52}")
    KeyWait, r
return
$d:: ; Alacrity (WWER)
    InstantCast("{Blind}{vk57 2}{vk45}{vk52}")
    KeyWait, d
return
#If

; =====================================================================
; НАБОР №2 (SHIFT QUEUE FIX — 0 МС)
; =====================================================================
#If WinActive("ahk_exe war3.exe") && !A_IsSuspended && GetKeyState("Shift", "P")
+$g:: Send {Blind}{vk51 2}{vk57}{vk52}
+$y:: Send {Blind}{vk51 3}{vk52}
+$f:: Send {Blind}{vk51 2}{vk45}{vk52}
+$b:: Send {Blind}{vk57 3}{vk52}
+$w:: Send {Blind}{vk57 2}{vk51}{vk52}
+$e:: Send {Blind}{vk45 3}{vk52}
+$q:: Send {Blind}{vk45 2}{vk57}{vk52}
+$v:: Send {Blind}{vk51}{vk57}{vk45}{vk52}
+$r:: Send {Blind}{vk45 2}{vk51}{vk52}
+$d:: Send {Blind}{vk57 2}{vk45}{vk52}
#If

InstantCast(keys) {
    global IsCasting
    IsCasting := 1
    Send, %keys%
    IsCasting := 0
}