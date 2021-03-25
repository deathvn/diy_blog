class BlogContent extends React.Component {
    constructor (props) {
        super(props);
        this.state = {
            showResults: false,
            toggleText: "Show Blog's content",
        }
    }

    handleShow = () => {
        if (this.state.showResults) {
            this.setState({
                showResults: false,
                toggleText: "Show Blog's content",
            })
        } else {
            this.setState({
                showResults: true,
                toggleText: "Hide Blog's content",
            })
        }
    }

    render () {
        return (
            <div>
                <input className="btn btn-info mb-3" type="submit" value={this.state.toggleText} onClick={this.handleShow} />
                { this.state.showResults ? <Results /> : null }
            </div>
        )
    }
    
}
  
function Results() {
    const mark = document.getElementById("raw-markdown").textContent.trim();
    return <div id ="blog-content" dangerouslySetInnerHTML={{ __html: marked(mark) }} />;
}
  
ReactDOM.render(<BlogContent />, document.getElementById("markdown-container"))