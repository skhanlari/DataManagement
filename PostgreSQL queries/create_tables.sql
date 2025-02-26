CREATE TABLE Badges (
    Id INTEGER PRIMARY KEY,
    UserId INTEGER,
    Name VARCHAR,
    Date DATE,
    Class INTEGER,
    TagBased BOOLEAN
);

CREATE TABLE Comments (
    Id INTEGER PRIMARY KEY,
    PostId INTEGER,
    Score INTEGER,
    Text VARCHAR,
    CreationDate DATE,
    UserId INTEGER,
    ContentLicense VARCHAR,
    UserDisplayName VARCHAR
);

CREATE TABLE PostHistory (
    Id INTEGER PRIMARY KEY,
    PostHistoryTypeId INTEGER,
    PostId INTEGER,
    RevisionGUID VARCHAR,
    CreationDate DATE,
    UserId INTEGER,
    Text VARCHAR,
    ContentLicense VARCHAR,
    UserDisplayName VARCHAR,
    Comment VARCHAR
);

CREATE TABLE PostLinks (
    Id INTEGER PRIMARY KEY,
    CreationDate DATE,
    PostId INTEGER,
    RelatedPostId INTEGER,
    LinkTypeId INTEGER
);

CREATE TABLE Posts (
    Id INTEGER PRIMARY KEY,
    PostTypeId INTEGER,
    AcceptedAnswerId INTEGER,
    CreationDate DATE,
    Score INTEGER,
    ViewCount INTEGER,
    Body VARCHAR,
    OwnerUserId INTEGER,
    LastEditorUserId INTEGER,
    LastEditDate DATE,
    LastActivityDate DATE,
    Title VARCHAR,
    Tags VARCHAR,
    AnswerCount INTEGER,
    CommentCount INTEGER,
    ContentLicense VARCHAR,
    OwnerDisplayName VARCHAR,
    ParentId INTEGER,
    ClosedDate DATE,
    CommunityOwnedDate DATE,
    LastEditorDisplayName VARCHAR,
    FavoriteCount INTEGER
);

CREATE TABLE Tags (
    Id INTEGER PRIMARY KEY,
    TagName VARCHAR,
    Count INTEGER,
    ExcerptPostId INTEGER,
    WikiPostId INTEGER
);

CREATE TABLE Users (
    Id INTEGER PRIMARY KEY,
    Reputation INTEGER,
    CreationDate DATE,
    DisplayName VARCHAR,
    LastAccessDate DATE,
    WebsiteUrl VARCHAR,
    Location VARCHAR,
    AboutMe VARCHAR,
    Views INTEGER,
    UpVotes INTEGER,
    DownVotes INTEGER,
    AccountId INTEGER
);

CREATE TABLE Votes (
    Id INTEGER PRIMARY KEY,
    PostId INTEGER,
    VoteTypeId INTEGER,
    CreationDate DATE,
    UserId INTEGER,
    BountyAmount INTEGER
);