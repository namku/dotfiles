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
" fzf window position
let g:fzf_preview_window = ['right:50%', 'ctrl-/']

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
