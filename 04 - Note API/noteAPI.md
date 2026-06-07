openapi: 3.0.3
info:
  title: NoteAPI
  version: 1.0.0
  description: |
    The Notekeep API allows users to manage personal notes. Use username=eve, password=letm3in for testing
  - url: https://ctf.nzcsc.org.nz/challenge4/api.php
paths:
  /login:
    post:
      summary: Log in with username and password
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                password:
                  type: string
      responses:
        '200':
          description: Login successful
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
        '401':
          description: Invalid credentials
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string

  /logout:
    post:
      summary: Log out current user session
      responses:
        '200':
          description: Successful logout
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string

  /notes:
    get:
      summary: Get all notes for the logged-in user
      responses:
        '200':
          description: List of user notes
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Note'
    post:
      summary: Create a new note
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                title:
                  type: string
                content:
                  type: string
      responses:
        '201':
          description: Note created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Note'

  /note/{id}:
    get:
      summary: Retrieve a single note by ID
      parameters:
        - name: id
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: A single note
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Note'
        '404':
          description: Note not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
    
  /profile:
    get:
      summary: Retrieve the logged-in user’s ID
      responses:
        '200':
          description: Current user ID
          content:
            application/json:
              schema:
                type: object
                properties:
                  user:
                    type: integer

  /health:
    get:
      summary: Check system health
      responses:
        '200':
          description: System health OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string

  /version:
    get:
      summary: Get API version
      responses:
        '200':
          description: Version info
          content:
            application/json:
              schema:
                type: object
                properties:
                  version:
                    type: string

  /settings:
    get:
      summary: Get user settings
      responses:
        '200':
          description: Settings for current user
          content:
            application/json:
              schema:
                type: object
                properties:
                  theme:
                    type: string

  /search:
    get:
      summary: Perform search
      responses:
        '200':
          description: Search placeholder
          content:
            application/json:
              schema:
                type: object
                properties:
                  search:
                    type: string

  /trash:
    get:
      summary: List items in trash
      responses:
        '200':
          description: Trash items
          content:
            application/json:
              schema:
                type: object
                properties:
                  trash:
                    type: array
                    items:
                      type: object

  /export:
    get:
      summary: Export data
      responses:
        '200':
          description: Export placeholder
          content:
            application/json:
              schema:
                type: object
                properties:
                  export:
                    type: string

  /import:
    post:
      summary: Import data
      responses:
        '200':
          description: Import placeholder
          content:
            application/json:
              schema:
                type: object
                properties:
                  import:
                    type: string

  /share:
    post:
      summary: Share a note
      responses:
        '200':
          description: Sharing disabled placeholder
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string

  /labels:
    get:
      summary: List user labels
      responses:
        '200':
          description: User labels
          content:
            application/json:
              schema:
                type: object
                properties:
                  labels:
                    type: array
                    items:
                      type: string

  /archive:
    get:
      summary: List archived notes
      responses:
        '200':
          description: Archived notes
          content:
            application/json:
              schema:
                type: object
                properties:
                  archive:
                    type: array
                    items:
                      type: object

  /reminders:
    get:
      summary: List reminders
      responses:
        '200':
          description: User reminders
          content:
            application/json:
              schema:
                type: object
                properties:
                  reminders:
                    type: array
                    items:
                      type: object

  /tags:
    get:
      summary: List user tags
      responses:
        '200':
          description: User tags
          content:
            application/json:
              schema:
                type: object
                properties:
                  tags:
                    type: array
                    items:
                      type: object

  /feedback:
    post:
      summary: Submit feedback
      responses:
        '200':
          description: Feedback response
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string

  /support:
    get:
      summary: Contact support
      responses:
        '200':
          description: Support contact
          content:
            application/json:
              schema:
                type: object
                properties:
                  contact:
                    type: string

  /debug:
    get:
      summary: Debug info
      responses:
        '200':
          description: Debug information
          content:
            application/json:
              schema:
                type: object
                properties:
                  env:
                    type: string

components:
  schemas:
    Note:
      type: object
      properties:
        id:
          type: integer
        title:
          type: string
        content:
          type: string
    User:
      type: object
      properties:
        id:
          type: integer
        username:
          type: string
