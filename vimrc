" 显示行号
set number
" 语法高亮显示
syntax on
set fileencodings=utf-8,gb2312,gbk,cp936,latin-1
set fileencoding=utf-8
set termencoding=utf-8
set fileformat=unix
set encoding=utf-8

" 设置缩进
set tabstop=4		" 设置制表符宽度为 4	
set softtabstop=4	" 设置（软）制表符宽度为 4	
set shiftwidth=4	" 设置缩进的空格数为 4
" set autoindent	" 设置自动缩进
set noautoindent	" 取消设置自动缩进, 与 autoindent 不可同时存在
set cindent		" 设置使用 C/C++ 语言的自动缩进方式
set cinoptions={0,1s,t0,n-2,p2s,(03s,=.5s,>1s,=1s,:1s	"设置C/C++语言的具体缩进方式（以我的windows风格为例）
" set smartindent

