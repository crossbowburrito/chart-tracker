import '/src/index.css';

function Navbar() {
    return (
        <nav className="navbar">
            <h1>Chorus Generator</h1>
            <div className="links">
                <a href="/songs">Top 50</a>
                <a href="/" style={{
                    color: "white",
                    backgroundColor: "#f1356d",
                    borderRadius: "8px"
                }}>New Chorus</a>
            </div>
        </nav>
    );
}

export default Navbar;