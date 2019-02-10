#### VIM

_Insert Mode_

- type `i` to enter Insert mode & enter text normally
- type `o` to enter insert mode & open a line below cursor
- type `O` to enter insert mode & open a line above cursor

_Command Mode_

- hit `Escape` to enter command mode

_Last-line mode_

- hit `:` from command mode to enter last-line mode.

_Movement in Vim_

- `h` moves the cursor left
- `j` moves the cursor down one line
- `k` moves the cursor up one line
- `l` moves the cursor to the right
- `0` moves the cursor to the beginning of the line
- `$` moves the cursor to the end of the line
- `w` moves the cursor forward one word
- `b` moves the cursor backwards one word
- `G` moves to the end of the file 
- `gg` moves to the beginning of the file
- Adding a digit will multiple the movement. So `5w` will move the cursor forward five words.

_Searching and Replacing in Vim_

- To search use `/` to search forward and `?` to search backwards, like `?lolcat`
- To move to the next instance of the search term use `n`
- To move to the previous instance, use: `N`
- To search and replace use: `%s/text/replacement/g`
- To search and replacement with confirmation use: `%s/text/replacement/gc`

_Editing commands in Vim_

- To start deleting use: `d`
- To delete a word: `dw`
- To delete from the cursor to the beginning of the line: `d0`
- To delete from the cursor to the end of the line: `d$`
- To delete to the beginning of the file: `dgg`
- To delete to the end of the file: `dG`
- Undo(intuitive): `u`
- Redo(last undo): `CTRL-r`

_Copying and Pasting in Vim_

- `v` will highlight one character at a time.
- `V` will highlight one line at a time.
- `Ctrl-v` will highlight by column.
- `p` will paste text after the current line.
- `P` will paste text on the current line.
- `y` will yank text into the copy buffer. 

_Save and Quit from Vim_

- `:w filename`
- `:wq filename`
- `q!` - To quit without saving
- `:w! filename` - To write over a file
- `Ctrl-z` - To leave Vim in the background

#### Word Completion and Abbrevations

_Avoid retyping! Word Completions make Vim very useful_

- `Ctrl-p` and `Ctrl-n` will search through the file and complete words.
- Enter command mode and use the `a b` command:
    + `:ab zkr Zonker`
    + `:ab orly O RLY?`  
- To use abbreviation, type "orly" and hit `SPACE`
- Note that Vim will convert any string "orly" into "O RLY" unless it is limit the abbreviation to insert mode using: `:iab orly O RLY?`
- To avoid an abbreviation, type `CTRL-v` after the string.
