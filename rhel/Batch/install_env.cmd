@echo off
CLS 
ECHO.
ECHO =============================
ECHO Running Admin shell
ECHO =============================

:checkPrivileges 
NET FILE 1>NUL 2>NUL
if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges ) 

:getPrivileges 
if '%1'=='ELEV' (shift & goto gotPrivileges)  
ECHO. 
ECHO **************************************
ECHO Invoking UAC for Privilege Escalation 
ECHO **************************************

setlocal DisableDelayedExpansion
set "batchPath=%~0"
setlocal EnableDelayedExpansion
ECHO Set UAC = CreateObject^("Shell.Application"^) > "%temp%\OEgetPrivileges.vbs" 
ECHO UAC.ShellExecute "!batchPath!", "ELEV", "", "runas", 1 >> "%temp%\OEgetPrivileges.vbs" 
"%temp%\OEgetPrivileges.vbs" 
exit 0

:gotPrivileges 
::::::::::::::::::::::::::::
:START
::::::::::::::::::::::::::::
setlocal & pushd .

REM Run shell as admin (example) - put here code as you like


:: ********************ENVIRONMENT VARIABLES START********************
@echo off
setlocal ENABLEDELAYEDEXPANSION
echo ====================================================
echo Setting up Environment Variables...
echo ====================================================
set SOFTWARE_INSTALLATION_LOC=\\sepdeliveries\SEPQAD_Share\Software_Installation
echo BDS Dev Environment Image Setup
set DEVENVIMG_INSTALLATION_LOC=%SOFTWARE_INSTALLATION_LOC%\utils
set SETX=%DEVENVIMG_INSTALLATION_LOC%\setx.exe
echo %SETX% SETX %SETX% /m
%SETX% SETX %SETX% /m

set JDK_VERSION=jdk1.7.0_80
echo %SETX% JDK_VERSION %JDK_VERSION% /m
%SETX% JDK_VERSION %JDK_VERSION% /m
set APP_HOME=D:\java
%SETX% APP_HOME %APP_HOME% /m
echo %SETX% APP_HOME %APP_HOME% /m
IF NOT EXIST %APP_HOME% mkdir %APP_HOME%
IF NOT EXIST %APP_HOME%\bea11 mkdir %APP_HOME%\bea11

::Setup JAVA_HOME and JAVA_HOME\bin in PATH
set JAVA_HOME=%APP_HOME%\%JDK_VERSION%
echo %SETX% JAVA_HOME %JAVA_HOME% /m
%SETX% JAVA_HOME %JAVA_HOME% /m

echo "%PATH%;"|findstr /C:"%JAVA_HOME%\bin" >nul 2>&1
if not errorlevel 1 (
   echo Path already contains %JAVA_HOME%\bin
) else (
   echo Adding to Path %JAVA_HOME%\bin and %APP_HOME%\apache-maven-3.0.4\bin and %APP_HOME%\apache-ant-1.8.3\bin
	%SETX% PATH "%APP_HOME%\apache-maven-3.0.4\bin;%JAVA_HOME%\bin;%PATH%;" /M
)

call set > D:\Java\set.log

echo ====================================================
echo Done!
echo ====================================================
:: ********************ENVIRONMENT VARIABLES END********************

:: ********************UNZIP JDK START********************
@echo off
echo ====================================================
echo Unzipping JDK in %JAVA_HOME%...
echo ====================================================
%DEVENVIMG_INSTALLATION_LOC%\unzip.exe -qo %SOFTWARE_INSTALLATION_LOC%\%JDK_VERSION%.zip -d %APP_HOME%
echo ====================================================
echo Done!
echo ====================================================
:: ********************UNZIP JDK END********************

:: ********************INSTALL ADDITIONAL SOFTWARE START********************
:: ********************UNZIP MAVEN START********************
@echo off
echo ====================================================
echo Unzipping Maven in %APP_HOME%\apache-maven-3.0.4...
echo ====================================================
%DEVENVIMG_INSTALLATION_LOC%\unzip.exe -qo %SOFTWARE_INSTALLATION_LOC%\apache-maven-3.0.4.zip -d %APP_HOME%\apache-maven-3.0.4
call mkdir %HOMEDRIVE%%HOMEPATH%\.m2
call mkdir %HOME%\..\..\%USERNAME%\.m2
IF EXIST G:\NUL GOTO USE_G
:USE_D
call copy /Y %SOFTWARE_INSTALLATION_LOC%\Windows7\.m2\settings_ddrive.xml %HOMEDRIVE%%HOMEPATH%\.m2\settings.xml
call copy /Y %SOFTWARE_INSTALLATION_LOC%\Windows7\.m2\settings_ddrive.xml %HOME%\..\..\%USERNAME%\.m2\settings.xml
GOTO END_MVN
:USE_G
call copy /Y %SOFTWARE_INSTALLATION_LOC%\Windows7\.m2\settings_gdrive.xml %HOMEDRIVE%%HOMEPATH%\.m2\settings.xml
call copy /Y %SOFTWARE_INSTALLATION_LOC%\Windows7\.m2\settings_gdrive.xml %HOME%\..\..\%USERNAME%\.m2\settings.xml
:END_MVN
echo ====================================================
echo Done!
echo ====================================================
:: ********************UNZIP MAVEN END********************

:: ********************UNZIP ANT START********************
echo ====================================================
echo Unzipping ANT in %APP_HOME%...
echo ====================================================
%DEVENVIMG_INSTALLATION_LOC%\unzip.exe -qo %SOFTWARE_INSTALLATION_LOC%\apache-ant-1.8.3.zip -d %APP_HOME%
echo ====================================================
echo Done!
echo ====================================================
:: ********************UNZIP ANT END********************

:: ********************UNZIP ECLIPSE START********************
@echo off
echo ====================================================
echo Unzipping Eclipse in %APP_HOME%...
echo ====================================================
%DEVENVIMG_INSTALLATION_LOC%\unzip.exe -qo %SOFTWARE_INSTALLATION_LOC%\eclipse_362_sep_new.zip -d %APP_HOME%\Eclipse-3.6-SEP
::Eclipse desktop shortcut
call %SOFTWARE_INSTALLATION_LOC%\Windows7\CREATE_SHORTCUT_VBS_BATCH.bat "D:\java\Eclipse-3.6-SEP\eclipse\eclipse.exe" Eclipse
echo ====================================================
echo Done!
echo ====================================================
:: ********************UNZIP ECLIPSE END********************

:: ********************UNZIP BCEL START********************
@echo off
echo ====================================================
echo Unzipping BCEL in %APP_HOME%...
echo ====================================================
echo %DEVENVIMG_INSTALLATION_LOC%\unzip.exe -qo "%SOFTWARE_INSTALLATION_LOC%\bcel 5.0\bcel-5.0.zip" -d %APP_HOME%\bcel-5.0
echo ====================================================
echo Done!
echo ====================================================
:: ********************UNZIP BCEL END********************

echo Close this window to continue.
pause