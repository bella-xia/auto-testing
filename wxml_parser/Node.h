#ifndef NODE_H
#define NODE_H

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <memory>
#include <optional>

#include "HTMLToken.h"

enum class NodeType
{
    ROOT_NODE,
    ELEMENT_NODE,
    ATTRIBUTE_NODE,
    DATA_NODE,
};

namespace Web
{

    class Node
    {
    public:
        // Constructor
        Node() : m_children(std::vector<Node *>()) {}

        virtual ~Node()
        {
            // std::cout << "default destructor called" << std::endl;
            for (Node *child_node : m_children)
            {
                delete child_node;
            }
        }

        // Add a child node
        void add_child(Node *child)
        {
            // child->m_parent = Node *(this);
            m_children.push_back(child);
        }

        size_t get_num_children() { return m_children.size(); }

        Node *get_children(long unsigned int idx)
        {
            return (idx < m_children.size() ? m_children[idx]
                                            : nullptr);
        }

        virtual std::string tag_name() const = 0;
        virtual NodeType type() const = 0;
        virtual std::string to_string() const = 0;

    protected:
        // Node * m_parent;                // Pointer to the parent node
        std::vector<Node *> m_children; // Children nodes
    };

    class RootNode : public Node
    {
    public:
        // Constructor
        RootNode() : Node() {}

        ~RootNode()
        {
        }

        virtual std::string tag_name() const override { return "#root {depth: 0}"; }
        virtual NodeType type() const override { return NodeType::ROOT_NODE; }
        virtual std::string to_string() const override { return tag_name(); }

        void add_root_child(RootNode *child)
        {
            Node::add_child(child);
            child->set_depth(m_depth + 1);
        }

        int get_depth() const { return m_depth; }
        void set_depth(int depth)
        {
            // ensure it is not root node, otherwise should not set depth
            assert(tag_name() != "#root");
            m_depth = depth;
        }

    private:
        int m_depth{0};
    };

    class ElementWrapperNode : public RootNode
    {
    public:
        // Constructor
        ElementWrapperNode(const std::tuple<std::string, bool> &tag_meta_info) : RootNode(),
                                                                                 m_tag_name(std::get<0>(tag_meta_info)),
                                                                                 m_has_end_tag(!(std::get<1>(tag_meta_info)))
        {
        }

        ~ElementWrapperNode()
        {
        }

        virtual std::string tag_name() const override
        {
            std::stringstream ss;
            ss << "element{" << m_tag_name << "}";
            return ss.str();
        }

        virtual NodeType type() const override { return NodeType::ELEMENT_NODE; }

        virtual std::string to_string() const override
        {
            std::stringstream ss;
            ss << "element{" << m_tag_name << "} {depth: " << get_depth() << "}";
            return ss.str();
        }

        bool has_end_tag() const { return m_has_end_tag; }
        std::string orig_tag_name() const { return m_tag_name; }

    private:
        std::string m_tag_name;
        bool m_has_end_tag;
    };

    class AttributeNode : public Node
    {
    public:
        AttributeNode(std::string attribute_name, std::string attribute_value = "") : Node(), m_name(attribute_name), m_value(attribute_value) {}

        ~AttributeNode()
        {
        }

        virtual std::string tag_name() const override
        {
            std::stringstream ss;
            ss << "attribute{" << m_name << "}";
            return ss.str();
        }

        virtual NodeType type() const override { return NodeType::ATTRIBUTE_NODE; }
        virtual std::string to_string() const override { return tag_name(); }

        std::string get_attribute_name() const { return m_name; }
        std::string get_attribute_values() const { return m_value; }

    private:
        std::string m_name;
        std::string m_value;
    };

    class DataNode : public Node
    {
    public:
        DataNode(std::string data, bool is_script = false) : Node(), m_data(data), m_is_script(is_script) {}

        ~DataNode()
        {
        }

        virtual std::string tag_name() const override
        {
            std::stringstream ss;
            if (m_is_script)
                ss << "script";
            ss << "data{" << m_data << "}";
            return ss.str();
        }

        virtual NodeType type() const override { return NodeType::DATA_NODE; }
        virtual std::string to_string() const override { return tag_name(); }

        std::string get_data() const { return m_data; }

    private:
        std::string m_data;
        bool m_is_script;
    };
}
#endif // NODE_H