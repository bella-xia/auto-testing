#include "WXMLDocumentParser.h"

// #define PARSER_DEBUG_TOKEN

namespace Web
{

    WXMLDocumentParser::WXMLDocumentParser() : m_root(new RootNode()), m_stack_of_open_elements(std::stack<RootNode *>())
    {
    }

    WXMLDocumentParser::WXMLDocumentParser(const std::u32string &input) : WXMLDocumentParser()
    {
        m_tokenizer.insert_input_text(input);
    }

    void WXMLDocumentParser::run()
    {
        HTMLToken token = HTMLToken();
        bool loop_flag = true;
        m_stack_of_open_elements.push(m_root);
        do
        {
            token = m_tokenizer.next_token();

#ifdef PARSER_DEBUG_TOKEN
            std::cout << " MODE: " << insertion_mode_name() << " EMIT: " << token.to_string() << std::endl;
#endif

            switch (token.m_type)
            {
            case (HTMLToken::Type::StartTag):
            {
                ElementWrapperNode *element_node = new ElementWrapperNode(token.get_tag_meta_info());
                m_stack_of_open_elements.top()->add_root_child(element_node);
                for (Attribute attr : token.m_tag.attributes)
                {
                    element_node->add_child(new AttributeNode(attr.name(), attr.value()));
                }
                if (element_node->has_end_tag())
                    m_stack_of_open_elements.push(element_node);
            }
            break;
            case (HTMLToken::Type::EndTag):
            {
                std::stringstream ss;
                ss << "element{" << token.m_tag.tag_name << "}";
                assert(ss.str() == m_stack_of_open_elements.top()->tag_name());
                for (Attribute attr : token.m_tag.attributes)
                {
                    m_stack_of_open_elements.top()->add_child(new AttributeNode(attr.name(), attr.value()));
                }
                m_stack_of_open_elements.pop();
            }
            break;
            case (HTMLToken::Type::Character):
            {
                for (std::tuple<std::string, bool> segment : segment_string(token.m_comment_or_character.data))
                {
                    m_stack_of_open_elements.top()->add_child(new DataNode(std::get<0>(segment), std::get<1>(segment)));
                }
            }
            break;
            case (HTMLToken::Type::Comment):
            {
            }
            break;
            case (HTMLToken::Type::DOCTYPE):
            {
            }
            break;
            case (HTMLToken::Type::EndOfFile):
            {
                loop_flag = false;
            }
            break;
            default:
                ASSERT_NOT_REACHED();
            }
        } while (loop_flag);

        // clear all references for now
        m_stack_of_open_elements.pop();
        assert(m_stack_of_open_elements.empty());

        print_ast(m_root);
    }
}