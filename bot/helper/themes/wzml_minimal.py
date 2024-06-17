#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Owner'
    ST_BN1_URL = 'https://t.me/acaatr'
    ST_BN2_NAME = 'Updates'
    ST_BN2_URL = 'https://t.me/Reaperzclub'
    ST_MSG = '''<b>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.</b>
<b>Type {help_command} to get a list of available commands</b>'''
    ST_BOTPM = '''<b>Now, This bot will send all your files and links here. Start Using ...</b>'''
    ST_UNAUTH = '''<b>You Are not authorized user! Deploy your own WZML-X Mirror-Leech bot</b>'''
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</b>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</b>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</b>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "<b>Help Guide Menu!</b>\n\n<b>NOTE: Click on any CMD to see more minor detalis.</b>"

    # async def stats(client, message):
    BOT_STATS = '''<b>BOT STATISTICS :</b>
<b>Bot Uptime :</b> {bot_uptime}

<b>RAM ( MEMORY ) :</b>
{ram_bar} {ram}%
<b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

<b>SWAP MEMORY :</b>
{swap_bar} {swap}%
<b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

<b>DISK :</b>
{disk_bar} {disk}%
<b>Total Disk Read :</b> {disk_read}
<b>Total Disk Write :</b> {disk_write}
<b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}
    
    '''
    SYS_STATS = '''<b><i>OS SYSTEM :</i></b>
<b>OS Uptime :</b> {os_uptime}
<b>OS Version :</b> {os_version}
<b>OS Arch :</b> {os_arch}

 <b>NETWORK STATS :</b>
<b>Upload Data:</b> {up_data}
<b>Download Data:</b> {dl_data}
<b>Pkts Sent:</b> {pkt_sent}k
<b>Pkts Received:</b> {pkt_recv}k
<b>Total I/O Data:</b> {tl_data}

<b>CPU :</b>
{cpu_bar} {cpu}%
<b>CPU Frequency :</b> {cpu_freq}
<b>System Avg Load :</b> {sys_load}
<b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
<b>Total Core(s) :</b> {total_core}
<b>Usable CPU(s) :</b> {cpu_use}
    '''
    REPO_STATS = ''' <b><i>REPO STATISTICS :</i></b>
<b>Bot Updated :</b> {last_commit}
<b>Current Version :</b> {bot_version}
<b>Latest Version :</b> {lat_version}
<b>Last ChangeLog :</b> {commit_details}

 <b>REMARKS :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = ''' <b><i>BOT LIMITATIONS :</i></b>
<b>Direct Limit :</b> {DL} GB
<b>Torrent Limit :</b> {TL} GB
<b>GDrive Limit :</b> {GL} GB
<b>YT-DLP Limit :</b> {YL} GB
<b>Playlist Limit :</b> {PL}
<b>Mega Limit :</b> {ML} GB
<b>Clone Limit :</b> {CL} GB
<b>Leech Limit :</b> {LL} GB

<b>Token Validity :</b> {TV}
<b>User Time Limit :</b> {UTI} / task
<b>User Parallel Tasks :</b> {UT}
<b>Bot Parallel Tasks :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<b>Restarting...</b>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = ''' <b>Restarted Successfully</b>
<b>Date:</b> {date}
<b>Time:</b> {time}
<b>TimeZone:</b> {timz}
<b>Version:</b> {version}'''
    RESTARTED = ''' <b>Bot Restarted!</b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<b>Starting Ping..</b>'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b>Task Started</b>
<b>Mode:</b> {Mode}
<b>By:</b> {Tag}\n\n"""
    LINKS_SOURCE = """ <b>Source:</b>
<b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            " <b><u>Task Started :</u></b>\n┃\n <b>Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           " <b><u>Leech Started :</u></b>\n┃\n <b>User :</b> {mention} ( #ID{uid} )\n <b>Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b>{Name}</b>\n\n'
    SIZE =                  '<b>Size: </b>{Size}\n'
    ELAPSE =                '<b>Elapsed: </b>{Time}\n'
    MODE =                  '<b>Mode: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '<b>Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '<b>Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '<b>By: </b>{Tag}\n\n'
    PM_BOT_MSG =            '<b>File(s) have been Sent above</b>'
    L_BOT_MSG =             '<b>File(s) have been Sent to Bot PM (Private)</b>'
    L_LL_MSG =              '<b>File(s) have been Sent. Access via Links></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '<b>Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '<b>SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '<b>Files: </b>{Files}\n'
    RCPATH =                '<b>Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '<b>By: </b>{Tag}\n\n'
    M_BOT_MSG =             '<b>Link(s) have been Sent to Bot PM (Private)</b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b>{Name}</b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =  '\n {Bar}'
    Speed= '<b> | {Speed}</b>'
    PROCESSED = '\n <b>Done:</b> {Processed}'
    STATUS =    '\n <b>Status:</b> <a href="{Url}">{Status}</a>'
    ETA =       '<b> | ETA:</b> {Eta}'
    SEEDERS= '<b> | S/L:</b> {Seeders}/'
    LEECHERS= '{Leechers}'
    MODE =      '\n <b>Mode:</b> {Mode}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n <b>Size: </b>{Size}'
    SEED_SPEED =     '\n <b>Speed: </b> {Speed} | '
    UPLOADED =                                     '<b>Uploaded: </b> {Upload}'
    RATIO =          '\n <b>Ratio: </b> {Ratio} | '
    TIME =                                         '<b>Time: </b> {Time}'
    SEED_ENGINE =    '\n <b>Engine:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n <b>Size: </b>{Size}'
    NON_ENGINE =     '\n <b>Engine:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =           '\n <b>User:</b> <code>{User}</code>'
    BTSEL =          ' | <b>TSel: {Btsel}</b>'
    CANCEL =         '\n <b>🎯{Cancel}</b>\n\n'

    ####------FOOTER--------
    TASKS =  '<b>Tasks:</b> {Tasks}\n'
    BOT_TASKS = ' <b>Tasks:</b> {Tasks}/{Ttask} | <b>AVL:</b> {Free}\n'
    FREE = '<b>Free:</b> {free}'
    uptime =' | <b>UPTM:</b> {uptime}'

    ###--------BUTTONS-------
    PREVIOUS = '⫷'
    REFRESH = '🤖'
    NEXT = '⫸'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b>{COUNT_NAME}</b>\n\n'
    COUNT_SIZE = ' <b>Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = ' <b>Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  ' <b>SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = ' <b>Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   ' <b>By: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<b>No Active Downloads!</b>
    
 <b>Bot Stats</b>
 <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
 <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = ''' <b><u>User Settings :</u></b>
        
<b> Name :</b> {NAME} ( <code>{ID}</code> )
<b> Username :</b> {USERNAME}
<b> Telegram DC :</b> {DC}
<b> Language :</b> {LANG}

 <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg'''

    UNIVERSAL = ''' <b><u>Universal Settings : {NAME}</u></b>

<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
<b> Daily Tasks :</b> <code>{DT}</code> per day
<b> Last Bot Used :</b> <code>{LAST_USED}</code>
<b> User Session :</b> <code>{USESS}</code>
<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
<b> Save Mode :</b> <code>{SAVE_MODE}</code>
<b> User Bot PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = ''' <b><u>Mirror/Clone Settings : {NAME}</u></b>

<b> RClone Config :</b> <i>{RCLONE}</i>
<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
<b> Mirror Remname :</b> <code>{MREMNAME}</code>
<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
<b> User TD Mode :</b> <i>{TMODE}</i>
<b> Total User TD(s) :</b> <i>{USERTD}</i>
<b> Daily Mirror :</b> <code>{DM}</code> per day'''

    LEECH = ''' <b><u>Leech Settings for {NAME}</u></b>

<b> Daily Leech : </b><code>{DL}</code> per day
<b> Leech Type :</b> <i>{LTYPE}</i>
<b> Custom Thumbnail :</b> <i>{THUMB}</i>
<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
<b> Leech Caption :</b> <code>{LCAPTION}</code>
<b> Leech Prefix :</b> <code>{LPREFIX}</code>
<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
<b> Leech Dumps :</b> <code>{LDUMP}</code>
<b> Leech Remname :</b> <code>{LREMNAME}</code>'''
