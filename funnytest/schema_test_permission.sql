
--
-- Table: permission
--
DROP TABLE IF EXISTS permission;
CREATE TABLE permission (
  id        SERIAL           NOT NULL,
  name      VARCHAR(80)      NOT NULL
)

DROP TABLE IF EXISTS group_permission;
CREATE TABLE group_permission (
  id                    SERIAL          PRIMARY KEY,
  permission_id         INTEGER         NOT NULL,
	created_at            TIMESTAMP       DEFAULT now() NOT NULL
);
