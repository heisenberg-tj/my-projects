; =====================================================================
; ArcaneKael v127.0 - Strict Miracle Delay Pack (Event 30ms / 15ms)
; AutoHotkey v1.1 - NO ORBS MIX - NO MOUSE FREEZE - 100% GAME STABLE
; =====================================================================
#NoEnv
#Persistent
#SingleInstance Force
#KeyHistory 0
#UseHook On
ListLines Off
SetBatchLines, -1
Process, Priority,, High
SendMode Event
SetKeyDelay, 30, 15

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
; НАБОР №1 (БЕЗ SHIFT)
; =====================================================================
#If WinActive("ahk_exe war3.exe") && !A_IsSuspended && !GetKeyState("Shift","P")
$g:: ; Ghost Walk (QQWR)
    IsCasting := 1
    Send {Blind}{vk51 2}{vk57}{vk52}
    IsCasting := 0
    KeyWait, g
return
$y:: ; Cold Snap (QQQR)
    IsCasting := 1
    Send {Blind}{vk51 3}{vk52}
    IsCasting := 0
    KeyWait, y
return
$f:: ; Ice Wall (QQER)
    IsCasting := 1
    Send {Blind}{vk51 2}{vk45}{vk52}
    IsCasting := 0
    KeyWait, f
return
$b:: ; EMP (WWWR)
    IsCasting := 1
    Send {Blind}{vk57 3}{vk52}
    IsCasting := 0
    KeyWait, b
return
$w:: ; Tornado (WWQR)
    IsCasting := 1
    Send {Blind}{vk57 2}{vk51}{vk52}
    IsCasting := 0
    KeyWait, w
return
$e:: ; Sun Strike (EEER)
    IsCasting := 1
    Send {Blind}{vk45 3}{vk52}
    IsCasting := 0
    KeyWait, e
return
$q:: ; Chaos Meteor (EEWR)
    IsCasting := 1
    Send {Blind}{vk45 2}{vk57}{vk52}
    IsCasting := 0
    KeyWait, q
return
$v:: ; Deafening Blast (QWER)
    IsCasting := 1
    Send {Blind}{vk51}{vk57}{vk45}{vk52}
    IsCasting := 0
    KeyWait, v
return
$r:: ; Forge Spirit (EEQR)
    IsCasting := 1
    Send {Blind}{vk45 2}{vk51}{vk52}
    IsCasting := 0
    KeyWait, r
return
$d:: ; Alacrity (WWER)
    IsCasting := 1
    Send {Blind}{vk57 2}{vk45}{vk52}
    IsCasting := 0
    KeyWait, d
return
#If

; =====================================================================
; НАБОР №2 (SHIFT QUEUE FIX)
; =====================================================================
#If WinActive("ahk_exe war3.exe") && !A_IsSuspended && GetKeyState("Shift","P")
+$g::
    IsCasting := 1
    SendMode Input
    Send {Blind}{vk51 2}{vk57}{vk52}
    SendMode Event
    IsCasting := 0
    KeyWait, g
return
+$y::
    IsCasting := 1
    SendMode Input
    Send {Blind}{vk51 3}{vk52}
    SendMode Event
    IsCasting := 0
    KeyWait, y
return
+$f::
    IsCasting := 1
    SendMode Input
    Send {Blind}{vk51 2}{vk45}{vk52}
    SendMode Event
    IsCasting := 0
    KeyWait, f
return
+$b::
    IsCasting := 1
    SendMode Input
    Send {Blind}{vk57 3}{vk52}
    SendMode Event
    IsCasting := 0
    KeyWait, b
return
+$w::
    IsCasting := 1
    SendMode Input
    Send {Blind}{vk57 2}{vk51}{vk52}
    SendMode Event
    IsCasting := 0
    KeyWait, w
return
+$e::
    IsCasting := 1
    SendMode Input
    Send {Blind}{vk45 3}{vk52}
    SendMode Event
    IsCasting := 0
    KeyWait, e
return
+$q::
    IsCasting := 1
    SendMode Input
    Send {Blind}{vk45 2}{vk57}{vk52}
    SendMode Event
    IsCasting := 0
    KeyWait, q
return
+$v::
    IsCasting := 1
    SendMode Input
    Send {Blind}{vk51}{vk57}{vk45}{vk52}
    SendMode Event
    IsCasting := 0
    KeyWait, v
return
+$r::
    IsCasting := 1
    SendMode Input
    Send {Blind}{vk45 2}{vk51}{vk52}
    SendMode Event
    IsCasting := 0
    KeyWait, r
return
+$d::
    IsCasting := 1
    SendMode Input
    Send {Blind}{vk57 2}{vk45}{vk52}
    SendMode Event
    IsCasting := 0
    KeyWait, d
return
#If