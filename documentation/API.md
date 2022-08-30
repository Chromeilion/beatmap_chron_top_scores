**Get Beatmap Leaderboard History**
----
  Returns JSON object containing an ordered list of top leaderboard spots
  in the order they happened across all mods.

* **URL**

  /getbeatmap

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `beatmap_id=integer`

* **Success Response:**

  * **Code:** 200 <br />
  *  **Content:** 
  ```
  {
    "status": status code,
    "data": {
      "scores": list of score objects ordered from oldest to newest.
    }
  }
  ```
 
* **Error Response:**

  * **Code:** 400 <br />
    **Given when:** beatmap_id is not an int, beatmap_id not provided.

  OR

  * **Code:** 500 <br />
    **Given when:** There's an issue connecting to osu API, other server 
                    issues.
