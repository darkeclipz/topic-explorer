# GTP Topic Explorer

Quicky explore a topic by having GPT generate a mini book about it.

  * It writes all the topics to Markdown files that are compatible with [tinyblog](https://tinyblog.gg).

## How to use

  1. Create a file `api.key` and paste in your OpenAI API key.
  2. Change the `subject` in `explore_topic.py`.
  3. Run `explore_topic.py`.
  4. Open the subject folder and run `tinyblog init`.
  5. Edit `settings.yml`:
     1. Set `blogName` to the subject.
     2. Set `defaultAuthor` to `gpt-4o` or whatever else you like.
     3. Set `generateTableOfContents` to `false`.
  6. Run `tinyblog serve` to start exploring!

