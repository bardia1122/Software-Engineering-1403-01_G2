import React, { useEffect,useContext,useState } from "react";
import { useQuill } from "react-quilljs";
import "quill/dist/quill.snow.css";
import "../styles/TextEditor.css";
import Quill from "quill";
import ReactDOMServer from 'react-dom/server'; 
import { FaTrash } from 'react-icons/fa';
import { SuggestionsContext } from "../contexts/SuggestionsContext";
import { ContentContext } from "../contexts/ContentContext";
import axios from "axios";
const Inline = Quill.import('blots/inline');
const Align = Quill.import('formats/align');
const Direction = Quill.import('formats/direction');
Quill.register(Align, true);
Quill.register(Direction, true);

class RedUnderlineBlot extends Inline {
    static create(value) {
        const node = super.create();
        node.classList.add('protected-red-underline');
        node.setAttribute("data-suggestion-index", String(value));
        return node;
    }

    static formats(node) {
        return node.getAttribute('data-suggestion-index');
    }
}

RedUnderlineBlot.blotName = 'redUnderline';
RedUnderlineBlot.tagName = 'span';
Quill.register(RedUnderlineBlot, true);


const Size = Quill.import('formats/size');
Size.whitelist = ['16px', '18px', '20px', '24px'];
Quill.register(Size, true);

const TextEditor = ({expandedIndex,setExpandedIndex,isOpen , setIsOpen}) => {
    const { suggestions, setSuggestions } = useContext(SuggestionsContext);
    const {content , setContent, setQuill} = useContext(ContentContext);
    const [debounceTimer, setDebounceTimer] = useState(null);
    const modules = {
        toolbar: {
            container: [
                [{ size: Size.whitelist }],
                [{ font: [] }],
                ['bold', 'italic', 'underline'],
                [{ 'color': [] }, { 'background': [] }],
                [{ align: [] }],
                [{ 'direction': 'rtl' }],
                [{ list: 'ordered' }, { list: 'bullet' }],
            ],
        },
        placeholder: "Start typing your content here..." 
    };

    const formats = [
        'size', 'font',
        'bold', 'italic', 'underline',
        'color', 'background',
        'align',
        'direction',
        'list',
        'redUnderline'
    ];

    const { quill, quillRef } = useQuill({ modules, formats });
    useEffect(()=>{
        setQuill(quill);
    },[quill])
    
    

    useEffect(() => {
        if (quill) {
            quill.format('align', 'right');
            quill.format('direction', 'rtl')

            quill.root.dataset.placeholder
            = "  متن خود را اینجا بنویسید...";
            const toolbar = quill.getModule('toolbar');
            const button = document.createElement('button');
            button.innerHTML = ReactDOMServer.renderToString(<FaTrash />);
            button.classList.add('ql-customTrash');
            button.onclick = () => {
                quill.setContents([]);
                quill.format('align', 'right');
                quill.format('direction', 'rtl')
                quill.root.dataset.placeholder 
                = "  متن خود را اینجا بنویسید...";
                button.blur();  
            };

            // Attach the button to the toolbar
            toolbar.container.appendChild(button);
            quill.on('text-change', () => {
                const text = quill.getText().trim();
                setContent(text);
                if (quill.getLength() > 1) {
                    quill.root.dataset.placeholder =''
                } else {
                    quill.root.dataset.placeholder
                     = "  متن خود را اینجا بنویسید...";
                }
            });
        }
    }, [quill]);
    useEffect(()=>{
        if (debounceTimer) clearTimeout(debounceTimer);
            setDebounceTimer(
                setTimeout(() => {
                    fetchSuggestions(content);
                }, 500)
            );
    },[content]);
    useEffect(() => {
        if (!quill) return;
        quill.formatText(0, quill.getLength(), 'redUnderline', false);

        suggestions.forEach((suggestion , index) => {
            quill.formatText(suggestion.start, suggestion.end-suggestion.start+1, 'redUnderline', String(index));
            
        });

        quill.root.addEventListener('click', (event) => {
            const clickedElement = event.target.closest('.protected-red-underline');
            if (clickedElement) {
                const clickedIndex = clickedElement.getAttribute('data-suggestion-index');
                setExpandedIndex(Number(clickedIndex));
                if(!isOpen){
                    setIsOpen(!isOpen);
                }
            }
        });
    }, [suggestions, quill,expandedIndex]);
    useEffect(()=>{

    },[suggestions])
    useEffect(()=>{
        setExpandedIndex(-1);
    },[suggestions])
    useEffect(()=>{
        if(!quill) return;

        quill.root.querySelectorAll('.protected-red-underline').forEach(el => {
            el.classList.remove('active');
        });

        const activeElement = quill.root.querySelector(
            `.protected-red-underline[data-suggestion-index="${expandedIndex}"]`
        );
        if (activeElement) {
            activeElement.classList.add('active');
        }
    },[expandedIndex])

    const fetchSuggestions = async (text) => {
        if (text.length===0) return;
        try {

            const response = await axios.post("http://127.0.0.1:8000/group3/optimize/", {
             text
            });
            setSuggestions(response.data.suggestions);
        } catch (error) {
            console.error("Error fetching suggestions:", error);
        }
    };

    return (
        <div className="text-editor">
            <div ref={quillRef} className="editor-textarea"></div>
        </div>
    );
};

export default TextEditor;
