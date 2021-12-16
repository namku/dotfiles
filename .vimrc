" Disable Background Color Erase (BCE) so that color schemes
" work properly when Vim is used inside tmux and GNU screen.
let &t_ut=''

set number
"set mouse=a
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

call plug#begin('~/.vim/plugged')

" Themes
"Plug 'morhetz/gruvbox'
"Plug 'arcticicestudio/nord-vim'
"Plug 'namku/Cake'
Plug 'sainnhe/gruvbox-material'
"Plug 'sainnhe/everforest'

" IDE
Plug 'easymotion/vim-easymotion'
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'

" same as gitlens vscode
Plug 'APZelos/blamer.nvim'

" Go
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }

" C#
Plug 'OmniSharp/omnisharp-vim'

" Autocomplete, Use release bracnh (recommend)
Plug 'neoclide/coc.nvim', {'branch': 'release'}
"
" Terraform
Plug 'hashivim/vim-terraform'

call plug#end()

" Golang options
let g:go_doc_popup_window = 1
let g:go_highlight_functions = 1
let g:go_highlight_operators = 1
"let g:go_highlight_build_constraints = 1
let g:go_highlight_structs = 1 
let g:go_highlight_methods = 1
let g:go_highlight_function_parameters = 1
let g:go_highlight_function_calls = 1
"let g:go_highlight_types = 1
let g:go_highlight_fields = 1
let g:go_highlight_variable_declarations = 1
let g:go_highlight_variable_assignments = 1

" gruvbox
"let g:gruvbox_contrast_dark = "hard"

let NERDTreeQuitOnOpen=1

" Terraform
"
" (Optionl) Enable terraform to apply 'terraform fmt' when it's save
let g:terraform_fmt_on_save=1

let g:LanguageClient_serverCommands = {
    \ 'terraform': ['terraform-ls', 'serve'],
    \ }

" (Optional) Enable terraform plan to be include in filter
" let g:syntastic_terraform_tffilter_plan = 1

" (Optional) Default: 0, enable(1)/disable(0) plugin's keymapping
" let g:terraform_completion_keys = 1

" (Optional) Default: 1, enable(1)/disable(0) terraform module registry completion
" let g:terraform_registry_module_completion = 0

let mapleader=" "

nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>

nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>

"source ~/coc.config

if executable('terraform-ls')
    au User lsp_setup call lsp#register_server({
        \ 'name': 'terraform-ls',
        \ 'cmd': {server_info->['terraform-ls', 'serve']},
        \ 'whitelist': ['terraform'],
        \ })
endif

" Themes config
set background=dark
colorscheme gruvbox-material
"colorscheme everforest

" Returns true if the color hex value is light for gruvbox-material
function! IsHexColorLight(color) abort
  let l:raw_color = trim(a:color, '#')

  let l:red = str2nr(substitute(l:raw_color, '(.{2}).{4}', '1', 'g'), 16)
  let l:green = str2nr(substitute(l:raw_color, '.{2}(.{2}).{2}', '1', 'g'), 16)
  let l:blue = str2nr(substitute(l:raw_color, '.{4}(.{2})', '1', 'g'), 16)

  let l:brightness = ((l:red * 299) + (l:green * 587) + (l:blue * 114)) / 1000

  return l:brightness > 155
endfunction
