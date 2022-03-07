" Disable Background Color Erase (BCE) so that color schemes
" work properly when Vim is used inside tmux and GNU screen.
let &t_ut=''

set number
set numberwidth=1
set clipboard=unnamed
syntax on
set showcmd
set ruler
set encoding=utf-8
set showmatch
set sw=2
set relativenumber
set laststatus=2

" Autocomplete
set wildmenu
set wildmode=longest:full,full

" Searching
set hlsearch " highlight matches
"set incsearch " incremental searching

so ~/.vim/plugins.vim
so ~/.vim/plugins_config.vim
so ~/.vim/mapping.vim

" Themes config
set background=dark
colorscheme gruvbox-material

"if executable('terraform-ls')
"    au User lsp_setup call lsp#register_server({
"        \ 'name': 'terraform-ls',
"        \ 'cmd': {server_info->['terraform-ls', 'serve']},
"        \ 'whitelist': ['terraform'],
"        \ })
"endif
