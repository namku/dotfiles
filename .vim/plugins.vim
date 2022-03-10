call plug#begin('~/.vim/plugged')

" Status bar
Plug 'maximbaz/lightline-ale'
Plug 'itchyny/lightline.vim'

" Themes
"Plug 'morhetz/gruvbox'
"Plug 'arcticicestudio/nord-vim'
"Plug 'namku/Cake'
Plug 'sainnhe/gruvbox-material'
"Plug 'sainnhe/everforest'

" IDE
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
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
