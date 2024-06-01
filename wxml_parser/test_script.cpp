#include "WXMLDocumentParser.h"
#include <iostream>
#include <fstream>

// #define TOKENIZER_DEBUG_MODE
#define PARSER_DEBUG_MODE

int main(int, char **)
{
    std::ifstream file("sample_html_files/index.wxml");

    if (!file.is_open())
    {
        std::cerr << "Unable to open file" << std::endl;
        return 1;
    }

    std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    std::wstring_convert<std::codecvt_utf8<char32_t>, char32_t> convert;
    std::u32string u32_content = convert.from_bytes(content);

#ifdef TOKENIZER_DEBUG_MODE
    Web::HTMLTokenizer tokenizer(u32_content);
    tokenizer.next_token();
#endif
#ifdef PARSER_DEBUG_MODE
    Web::WXMLDocumentParser parser(u32_content);
    parser.run();
#endif
    return 0;
}