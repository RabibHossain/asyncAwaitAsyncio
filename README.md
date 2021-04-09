<b>What is synchronous code?</b><br>
Synchronous code:
<ul>
  <li>Runs functions one after another</li>
</ul>

<b>What is asynchronous code?</b><br>
Asynchronous code:
<ul>
  <li>Runs multiple functions seemingly in parallel
    <ul>
        <li>In a single process</li>
        <li>Without threads</li>
    </ul>
  </li>
  <li>Requires cooporative, well-behaving functions
    <ul>
      <li>Functions that reqularly suspend by awaiting something</li>
    </ul>
  </li>
  <li>Should not use functions
    <ul>
        <li>No time.sleep()</li>
        <li>No socket.*</li>
        <li>asyncio provides non-blocking alternatives for many of these functions</li>
    </ul>
  </li>
</ul>
