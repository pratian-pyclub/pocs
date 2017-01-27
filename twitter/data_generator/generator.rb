require 'yaml'
require 'twitter'

PWD = File.expand_path(File.dirname(__FILE__))

cred = YAML::load_file("#{PWD}/cred.yml")

client = Twitter::REST::Client.new do |config|
  config.consumer_key        = cred["consumer_key"]
  config.consumer_secret     = cred["consumer_secret"]
  config.access_token        = cred["access_token"]
  config.access_token_secret = cred["access_token_secret"]
end

data = []
client.search("#jallikattu, OR #jallikattubill, OR #ammendpca since:2017-01-07 until:2017-01-21", result_type: "recent").take(10).collect do |tweet|
  data.push(
    {
      username: tweet.user.screen_name,
      text: tweet.full_text,
      url: tweet.uri.to_s,
      created_at: tweet.created_at,
      favorite_count: tweet.favorite_count,
      retweet_count: tweet.retweet_count,
      hashtags: tweet.hashtags?,
      media: tweet.media?
    }
  )
  # we don't want Twitter to ratelimit us
  sleep 0.1
end

File.open("#{PWD}/data.yml", 'a') do |file|
  file.write data.to_yaml
end
