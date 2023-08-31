import { useState, useEffect } from 'react';




function SongList() {
    const [songs, setSongs] = useState([]);

    useEffect(() => {
        const fetchSongs = async () => {
            try {
                const res = await fetch('http://localhost:5000/songs');
                const data = await res.json();
                setSongs(data);
            } catch (err) {
                console.log(err);
            }
        };

        fetchSongs();
    }, []);

    return (
        <div>
            <h1>Top 50 Songs</h1>
            <table>
                <thead>
                    <tr>
                        <th>Position</th>
                        <th>Title</th>
                        <th>Artist</th>
                        <th>Release Date</th>
                        <th>Stream</th>
                    </tr>
                </thead>
                <tbody>
                    {songs.map((song, index) => (
                        <tr key={index}>
                            <td>{index + 1}</td>
                            <td>{song.name}</td>
                            <td>{song.artist}</td>
                            <td>{song.release_date}</td>
                            <td><a href="#">S</a><a href ="#2"> A </a><a href="#3"> Y</a></td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default SongList;