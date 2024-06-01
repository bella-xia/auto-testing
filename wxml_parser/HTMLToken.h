#ifndef HTMLTOKEN_H
#define HTMLTOKEN_H

#include "Attriute.h"
#include <cassert>
#include <tuple>
#include <vector>

namespace Web
{

    class HTMLToken
    {
        friend class HTMLTokenizer;
        friend class WXMLDocumentParser;

    public:
        enum class Type
        {
            DOCTYPE,
            StartTag,
            EndTag,
            Comment,
            Character,
            EndOfFile
        };

        HTMLToken();
        Type type() const { return m_type; }
        std::tuple<std::string, bool> get_tag_meta_info() const;
        std::string to_string() const;

    private:
        Type m_type{Type::EndOfFile};

        // TYPE::DOCTYPE
        struct
        {
            std::string m_name;
            std::string m_doctype_public_identifier;
            std::string m_doctype_system_idenfier;

            bool m_force_quirks_flag{false};

        } m_doctype;

        // TYPE::StartTag
        // TYPE::ENdTag
        struct
        {
            std::string tag_name;
            bool self_closing{false};
            std::vector<Attribute> attributes{std::vector<Attribute>()};
        } m_tag;

        struct
        {
            std::string data;
        } m_comment_or_character;
    };
}

#endif // HTMLTOKEN_H