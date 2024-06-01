#ifndef WXMLDocumentParser_H
#define WXMLDocumentParser_H

#include <cassert>
#include "HTMLTokenizer.h"

/*
#define ENUMERATE_INSERTION_MODES               \
    __ENUMERATE_INSERTION_MODE(Initial)         \
    __ENUMERATE_INSERTION_MODE(BeforeHTML)      \
    __ENUMERATE_INSERTION_MODE(BeforeHead)      \
    __ENUMERATE_INSERTION_MODE(InHead)          \
    __ENUMERATE_INSERTION_MODE(InHeadNoscript)  \
    __ENUMERATE_INSERTION_MODE(AfterHead)       \
    __ENUMERATE_INSERTION_MODE(InBody)          \
    __ENUMERATE_INSERTION_MODE(Text)            \
    __ENUMERATE_INSERTION_MODE(InTable)         \
    __ENUMERATE_INSERTION_MODE(InTableText)     \
    __ENUMERATE_INSERTION_MODE(InCaption)       \
    __ENUMERATE_INSERTION_MODE(InColumnGroup)   \
    __ENUMERATE_INSERTION_MODE(InTableBody)     \
    __ENUMERATE_INSERTION_MODE(InRow)           \
    __ENUMERATE_INSERTION_MODE(InCell)          \
    __ENUMERATE_INSERTION_MODE(InSelect)        \
    __ENUMERATE_INSERTION_MODE(InSelectInTable) \
    __ENUMERATE_INSERTION_MODE(InTemplate)      \
    __ENUMERATE_INSERTION_MODE(AfterBody)       \
    __ENUMERATE_INSERTION_MODE(InFrameset)      \
    __ENUMERATE_INSERTION_MODE(AfterFrameset)   \
    __ENUMERATE_INSERTION_MODE(AfterAfterBody)  \
    __ENUMERATE_INSERTION_MODE(AfterAfterFrameset)
    */

namespace Web
{
    class WXMLDocumentParser
    {

    public:
        WXMLDocumentParser();
        WXMLDocumentParser(const std::u32string &input);

        ~WXMLDocumentParser()
        {
            delete m_root;
        }

        HTMLToken next_token() { return m_tokenizer.next_token(); }

        void run();

    private:
        RootNode *m_root;
        std::stack<RootNode *> m_stack_of_open_elements;
        HTMLTokenizer m_tokenizer;

        /*
                enum class InsertionMode
                {
        #define __ENUMERATE_INSERTION_MODE(x) x,
                    ENUMERATE_INSERTION_MODES
        #undef __ENUMERATE_INSERTION_MODE
                };

                std::string insertion_mode_name() const
                {
                    switch (m_insertion_mode)
                    {
        #define __ENUMERATE_INSERTION_MODE(x) \
            case InsertionMode::x:            \
                return #x;
                        ENUMERATE_INSERTION_MODES
        #undef __ENUMERATE_INSERTION_MODE
                    }
                    ASSERT_NOT_REACHED();
                }

                InsertionMode insertion_mode() const { return m_insertion_mode; }
                InsertionMode m_insertion_mode{InsertionMode::InBody};

                void handle_initial(const HTMLToken &current_token);
                void handle_before_html(const HTMLToken &current_token);
                void handle_before_head(const HTMLToken &current_token);
                void handle_in_head(const HTMLToken &current_token);
                void handle_in_head_no_script(const HTMLToken &current_token);
                void handle_after_head(const HTMLToken &current_token);
                void handle_in_body(const HTMLToken &current_token);
                void handle_text(const HTMLToken &current_token);
                */
    };
}

#endif // WXMLDocumentParser_H