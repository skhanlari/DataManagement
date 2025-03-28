ALTER TABLE Comments
ADD CONSTRAINT FK_Comments_PostId FOREIGN KEY (PostId)
REFERENCES Posts(Id);

ALTER TABLE PostHistory
ADD CONSTRAINT FK_PostHistory_PostId FOREIGN KEY (PostId)
REFERENCES Posts(Id)
ON DELETE SET NULL,
ADD CONSTRAINT FK_PostHistory_UserId FOREIGN KEY (userid)
REFERENCES Users(Id)
ON DELETE SET NULL;

ALTER TABLE PostLinks
ADD CONSTRAINT FK_PostLinks_PostId FOREIGN KEY (PostId)
REFERENCES Posts(Id),
ADD CONSTRAINT FK_PostLinks_RelatedPostId FOREIGN KEY (RelatedPostId)
REFERENCES Posts(Id);

ALTER TABLE Votes
ADD CONSTRAINT FK_Votes_PostId FOREIGN KEY (PostId)
REFERENCES Posts(Id),
ADD CONSTRAINT FK_Votes_UserId FOREIGN KEY (UserId)
REFERENCES Users(Id)
ON DELETE SET NULL;

ALTER TABLE badges
ADD CONSTRAINT FK_Badges_UserId FOREIGN KEY (userid)
REFERENCES Users(Id);


-- EXECUTE AFTER REMOVING THE NOT PRESENT
ALTER TABLE Posts
ADD CONSTRAINT FK_Posts_AcceptedAnswerId FOREIGN KEY (AcceptedAnswerId)
REFERENCES Posts(Id)
ON DELETE SET NULL,
ADD CONSTRAINT FK_Posts_ParentId FOREIGN KEY (parentid)
REFERENCES Posts(Id)
ON DELETE SET NULL,
ADD CONSTRAINT FK_Posts_OwnerUserId FOREIGN KEY (owneruserid)
REFERENCES Users(Id)
ON DELETE SET NULL;